#include "stm32f4xx.h"
#define PLL_M   4
#define PLL_N   84
#define PLL_P   0 //PLL_P = 2


void systemClockConfig(void)
{
    //enable HSE nd wait for HSE to become ready
    RCC->CR |= RCC_CR_HSEON;
    while(!(RCC->CR & RCC_CR_HSERDY));
    
    //enable power clock and voltage regulator 
    RCC->APB1ENR |= RCC_APB1ENR_PWREN;
    PWR->CR |= PWR_CR_VOS;
    
    //configure th flash prefetch and latency related setting
    FLASH->ACR = FLASH_ACR_ICEN|FLASH_ACR_DCEN|FLASH_ACR_LATENCY_5WS|FLASH_ACR_PRFTEN;
    
    //configure the prescalers HCLK PCLK1 PCLK2
    //AHB prescaler = /1
    RCC->CFGR |= RCC_CFGR_HPRE_DIV1;
    //APB1 prescaler = /2
    RCC->CFGR |= RCC_CFGR_PPRE1_DIV2;
    //APB2 prescaler = /1
    RCC->CFGR |= RCC_CFGR_PPRE2_DIV1;
    
    //configure main PLL
    RCC->PLLCFGR = (PLL_M<<0)|(PLL_N<<6)|(PLL_P<<16)|(RCC_PLLCFGR_PLLSRC_HSE);
    
    //enable PLL and wait it to become ready
    RCC->CR |= RCC_CR_PLLON;
    while(!(RCC->CR & RCC_CR_PLLRDY));
    
    //set clock source and wait it to be set
    RCC->CFGR |= RCC_CFGR_SW_PLL;
    while((RCC->CFGR & RCC_CFGR_SWS) != RCC_CFGR_SWS_PLL);
    
}


void TIM2_config(void)
{
    //enable timer2 clock
    RCC->APB1ENR |= (1<<0);
    
    //set the prescaler and ARR
    TIM2->PSC = 84-1;   //  84MHz/84 = 1MHz = 1us delay
    TIM2->ARR = 0xffff;
    
    //enable the counter in timer2
    TIM2->CR1 |= (1<<0);
    while(! (TIM2->SR &(1<<0)));   //UIF bit (update interrupt pending) this bit is set by hardware when the registers are update
}


void delay_us (uint16_t us)
{
    //reset counter
    TIM2->CNT = 0;
    while(TIM2->CNT < us);
}

void delay_ms (uint16_t ms)
{
    for (uint16_t i=0;i<ms;i++)
    {
        delay_us(1000);
    }
}



void ADC_Init(void)
{
    /*max clock of ADC is 36MHz
    since all ADCs are connected to APB2 clock = 84MHz
    to achieve the Max ADC clock we must set prescaler to /4   */
    
    //enable GPIOA and ADC1 clock
    RCC->AHB1ENR |= (1<<0);
    RCC->APB2ENR |= (1<<8);
    
    /*set the prescaler in common control register(CCR)
    set 16,17 bits ADCPRE to 01 to set prescaler=/4  */
    ADC1_COMMON->CCR |= (1<<16);

   //set scan mode and resolution in CR1
    ADC1->CR1 |= (1<<8); //set 8th bit to 1 to enable scan mode
    ADC1->CR1 &= ~(1<<24); //set 25:24 = 0:0 to use 12 bit resolution
    
    //set continuous conversion ,End of Conversion,data alignment in CR2
    ADC1->CR2 |= ((1<<1) | (1<<10)); //10th bit to get end of conversion and 1st bit to set continuous conversion
    ADC1->CR2 &= ~(1<<11); //set 11th bit to 0 for right alignment
    
    /*set sampling time for channels in ADC_SMPRx
    Tconv = (sampling time + 12 cycles)/ADCCLK
    ADCCLK = APB2CLK/Prescaler            
    as we are not using any ADC device we use 3cycles[23:20]=000(sampling time)
    set 000 at channel 1,4 as we are using PA1 and PA4 channels*/
    ADC1->SMPR2 &= ~((7<<3) | (7<<12));
    
    /*set regular channel sequence length in ADC_SQR1
    L[3:0] = 23:20 it denotes number of channels used as we 
    are using 3 channels set 0010*/
    ADC1->SQR1 |= (2<<20);
    
    //set respective GPIO pins in analog mode send 11 to MODER1,4
    GPIOA->MODER |= ((3<<2)|(3<<8));
    
    //enable DMA and continuous request for ADC1 
    ADC1->CR2 |= ((1<<8)|(1<<9));
    
    //channel sequence
    ADC1->SQR3 |= ((1<<0)|(4<<5)); //SEQ1,SEQ2 for channel 1,4
    ADC1->SQR3 |= (18<<10); //SEQ3 for channel 18
    
    /*Tconv = (sampling time + 12 cycles)/ADCCLK
     ADCCLK = APB2CLK/prescaler = 84MHz/4 = 21MHz
     min sampling time of internal temp sensor is 10us
     set the sampling frequency greater than min sampling time
     Tconv = (480 cycles+12 cycles)/21MHz = 23.4us > 10us
     for 480 cycles set 111 at SMP18[2:0] = 26:24*/
     ADC1->SMPR1 |= (7<<24);
     
     //set TSVREFE bit to wake up the sensor
     ADC1_COMMON->CCR |= (1<<23);  
    
}



void ADC_Enable(void)
{
    //enable ADC by setting ADON bit in CR2
    ADC1->CR2 |= (1<<0);
    //wait ADC to stabilize (~10us)
    uint32_t delay = 10000;
    while(delay--);
    
}



void ADC_Start(void)
{   
    //clear status register
    ADC1->SR = 0;
    
    //set SWSRT bit in CR2 to start ADC
    ADC1->CR2 |= (1<<30);
    
}

void DMA_Init (void)
{
    //enable DMA2 clock
    RCC->AHB1ENR |= (1<<22);
    
    //set data direction 00 = peripheral to memory
    DMA2_Stream0->CR &= ~(3<<6);
    
    //select circular mode
    DMA2_Stream0->CR |= (1<<8);
    
    //enable memory address increment
    DMA2_Stream0->CR |= (1<<10);
    
    /*set peripheral(PSIZE) and memory data size(MSIZE)
    since we are using the 12 bit ADC use 16 bit size
    therefore set 01 to bit 12:11 and 14:13*/
    DMA2_Stream0->CR |= ((1<<11)|(1<<13));
    
    //select the channel for the stream
    DMA2_Stream0->CR &= ~(7<<25); //set 000 to 27:25
    
}

void DMA_config(uint32_t srcAdd,uint32_t destAdd,uint16_t size)
{
    //set size of data transfer
    DMA2_Stream0->NDTR = size;
    
    //src address is peripheral address
    DMA2_Stream0->PAR = srcAdd;
    
    //destination address is memory address
    DMA2_Stream0->M0AR = destAdd;
    
    //enable DMA stream
    DMA2_Stream0->CR |= (1<<0);
    
}

uint16_t RxData[3];
float temp;

int main()
{
    systemClockConfig();
    TIM2_config();
    
    ADC_Init();
    ADC_Enable();
    
    DMA_Init();
    DMA_config((uint32_t) &ADC1->DR , (uint32_t)RxData,3);
    
    ADC_Start();
    
    while(1)
    {
        //Temperature (in °C) = {(VSENSE – V25) / Avg_Slope} + 25
        //V25 = voltage at 25°C = 0.76V ang Avg_Slope = 2.5mV/°C
        temp = (((float)(3.3*RxData[2]/(float)4095)-0.76)/0.025) + 25; 
    }
   
}

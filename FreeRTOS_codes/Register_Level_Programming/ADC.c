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
    ADC1->SMPR2 &= ~((1<<3) | (1<<12));
    
    /*set regular channel sequence length in ADC_SQR1
    L[3:0] = 23:20 it denotes number of channels used as we 
    are using 2 channels set 0001*/
    ADC1->SQR1 |= (1<<20);
    
    //set respective GPIO pins in analog mode send 11 to MODER1,4
    GPIOA->MODER |= ((3<<2)|(3<<8));
    
}



void ADC_Enable(void)
{
    //enable ADC by setting ADON bit in CR2
    ADC1->CR2 |= (1<<0);
    //wait ADC to stabilize (~10us)
    uint32_t delay = 10000;
    while(delay--);
    
}



void ADC_Start(int channel)
{
    //set channel sequence in SQR register
    ADC1->SQR3 = 0; //clear sequence register
    ADC1->SQR3 |= (channel<<0);
    
    //clear status register
    ADC1->SR = 0;
    
    //set SWSRT bit in CR2 to start ADC
    ADC1->CR2 |= (1<<30);
    
}



void ADC_WaitforConv(void)
{
    //bit 1 EOC in SR (regular channel end of conversion
    while(!(ADC1->SR & (1<<1)));
}



uint16_t ADC_GetValue(void)
{
    return ADC1->DR; //read data register
}




void ADC_Disable(void)
{
    ADC1->CR2 &= ~(1<<0); //clear ADON bit in CR2
}


uint16_t ADC_VAL[2] = {0,0};

int main()
{
    systemClockConfig();
    ADC_Init();
    ADC_Enable();
    
    while(1)
    {
        ADC_Start(1);
        ADC_WaitforConv();
        ADC_VAL[0] = ADC_GetValue();
        
        ADC_Start(4);
        ADC_WaitforConv();
        ADC_VAL[1] = ADC_GetValue();
            
    }
    
}

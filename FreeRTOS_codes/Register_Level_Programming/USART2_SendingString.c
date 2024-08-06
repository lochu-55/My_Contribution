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

void USART2_config (void)
{
    //enable UART clock and GPIO clock PA2-Tx PA3-Rx
    RCC->APB1ENR |= (1<<17);
    RCC->AHB1ENR |= (1<<0);
    
    //configure UART pins(PA2,PA3) for alternate function
    //alternate mode = 10 , set 2 at 4,6th pos bits
    GPIOA->MODER |= (2<<4)|(2<<6);
    
    //set high speed(11) for PA2,PA3 pins that is send 3 to 4,6 pos bits
    GPIOA->OSPEEDR |= (3<<4)|(3<<6);
    
    //AF7 is for USART2 since I am using PA2,PA3 use AFRL register
    //write 7(0111) to AFRL2,AFRL3 (pin8,12)
    GPIOA->AFR[0] |= (7<<8)|(7<<12);
    
    //enable USART by writing UE bit(13th bit) in USART_CR1 register
    USART2->CR1 = 0x00; //clear all
    USART2->CR1 |= (1<<13);
    
    //program M bit (12th bit) in USART2->CR1 to define word length
    USART2->CR1 &= ~(1<<12); //for 8 data bits send 0 to M bit
    
    /*select the baud rate using USART_BRR register
    tx/rx baud = fclk/(8*(2-OVER8)*USARTDIV)
    115200 = 42MHz/8*(2-0)* USARTDIV
    USARTDIV = 22.786
    DIV_Fraction = 16*0.786 = 12.6 ~= 13
    DIV_mantissa = 22
    write 13 to 0th pos and 22 to 4th pos bits
    */
       // Select the baud rate using USART_BRR register
    USART2->BRR |= (13<<0) | (22<<4);
    
    //enable the tx/rx by setting TE,RE bits in USART_CR1
    USART2->CR1 |= (1<<2)|(1<<3);
    
}

void UART_SendChar(uint8_t ch)
{
    /*write data to send in USART_DR register , this cleqar
    TxE bit , repeat for each data to be transmitted in case 
    of single buffer. After writing the last data into USART_DR, 
    wait till TC=1, indicate transmission of last frame is completed*/ 
    
    USART2->DR = ch;
    while(!(USART2->SR & (1<<6)));
    
}

void UART_SendString(char *str)
{
    while(*str) UART_SendChar(*str++);
}

int main (void)
{
    systemClockConfig();
    TIM2_config();
    USART2_config();
    
    while(1)
    {
        UART_SendString("Lochu\n");
        delay_ms(1000);
    }
}

#include "stm32f4xx.h"
#define PLL_M   16
#define PLL_N   336
#define PLL_P   1


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


void GPIO_config(void)
{
    //enable GPIOA clock
    RCC->AHB1ENR |= (1<<0);
    
    //set PA5 as output
    GPIOA->MODER |= (1<<10);
    
    //config output mode as push pull
    GPIOA->OTYPER &= ~(1<<5);
    
    //set speed of the pin
    GPIOA->OSPEEDR |= (1<<11);
    
    //set the pull up or pull down
    GPIOA->PUPDR &= ~((1<<10) | (1<<11));
    
}


int main(void)
{
    systemClockConfig();
    TIM2_config();
    GPIO_config();
    
    while(1)
    {
        GPIOA->BSRR |= (1<<5);
        delay_ms(1000);
        GPIOA->BSRR |= (1<<21);
        delay_ms(1000);
    }
}



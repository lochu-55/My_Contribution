#include "stm32f4xx.h"

void GPIO_config(void)
{
    RCC->AHB1ENR |= (1<<2);
    RCC->AHB1ENR |= (1<<0);
    
    GPIOA->MODER |= (1<<10);
    GPIOC->MODER &= ~(3 << 26);
    GPIOC->PUPDR |= (1 << 26);

}

void Interrupt_config(void)
{
    RCC->APB2ENR |= (1<<14);
    SYSCFG->EXTICR[3] |= (1<<5);
    EXTI->IMR |= (1<<13);
    EXTI->RTSR |= (1<<13);
    EXTI->FTSR &= ~(1<<13);
    NVIC_SetPriority(EXTI15_10_IRQn,1);
    NVIC_EnableIRQ(EXTI15_10_IRQn);
    
}

int flag=0;
int count=0;
void EXTI15_10_IRQHandler(void)
{
    if(EXTI->PR &(1<<13))
    {
        EXTI->PR |= (1<<13);
        flag=1;
    }
}


void delay(uint32_t time)
{
    while(time--)
    {}
}


int main()
{
    GPIO_config();
    Interrupt_config();
    while(1)
    {
        if(flag)
        {
            delay(100000);
            count++;
            flag=0;
            GPIOA->ODR ^= (1<<5);
        }
           
    }
}

#include "stm32f4xx.h"

void GPIO_config(void)
{
    //enable clock for GPIOA and GPIOC
    RCC->AHB1ENR |= (1<<2);
    RCC->AHB1ENR |= (1<<0);
    
    //set GPIOA as output and GPIOC as input
    GPIOA->MODER |= (1<<10);
    GPIOC->MODER &= ~(3 << 26);
    
    //enable pull up on GPIOC
    GPIOC->PUPDR |= (1 << 26);

}

void Interrupt_config(void)
{
    //enable system config controller clock in APB2
    RCC->APB2ENR |= (1<<14);
    
    //configure EXTI register in SYSCFG for 13th pin
    SYSCFG->EXTICR[3] |= (1<<5);
    
    //disable mask on EXTI
    EXTI->IMR |= (1<<13);
    
    //enable rising edge and disable falling edge
    EXTI->RTSR |= (1<<13);
    EXTI->FTSR &= ~(1<<13);
    
    //set the interrupt priority for 13th interrupt line
    NVIC_SetPriority(EXTI15_10_IRQn,1);
    
    //enable the interrupt
    NVIC_EnableIRQ(EXTI15_10_IRQn);
    
}

int flag=0;
int count=0;
void EXTI15_10_IRQHandler(void)
{
    if(EXTI->PR &(1<<13))  //check the pin ,which triggered the interrupt
    {
        EXTI->PR |= (1<<13); //clear the pending bit
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

#include "stm32f401xe.h"
/*void GPIO_config(void);

uint32_t count=0,i;

int main()
{
    GPIO_config();
    RCC->APB2ENR = 0x00004000;
    SYSCFG->EXTICR[3] &= 0xFFFFFF2F;
    EXTI->IMR =0X00002000;
    EXTI->RTSR &=0XFFFFDFFF;
    EXTI->FTSR |=0X00002000;
    NVIC->ISER[1] = 0X00000100;
    
    
}

void GPIO_config(void){
    RCC->AHB1ENR = 0X00000005;
    GPIOA->MODER = 0X00000400;
    GPIOA->OSPEEDR = 0X00000400;
    GPIOC->MODER &= 0XF3FFFFFF;
    GPIOA->PUPDR &= 0XF3FFFFFF; 
       
}


void EXTI15_10_IRQHandler() {
    EXTI->PR = 0X00002000;
    if(count==0){                          
        for(i=0;i<100000;i++);
        count++;
    }
     else {                                    
         for(i=0;i<100000;i++);
         count--;
     }         
}*/


int main(void)
{
    //uint32_t i;
    RCC->AHB1ENR |= 0x00000001;  
    
    GPIOA->MODER |= 0x00000400 ;
    
    GPIOA->OSPEEDR |= 0x00000400;
   
    while(1)
    {
    GPIOA->ODR = 0x00000020;
    for(int i=0 ;i<5000000;i++);
    GPIOA->ODR = 0x00000000;
    for(int i=0 ;i<5000000;i++);
    
    }
}


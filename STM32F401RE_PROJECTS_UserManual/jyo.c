#include "stm32f401xe.h"
void GPIO_config(void);

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
    if(count==0){                           /*turn on the leds for first push*/
        GPIOA->ODR = 0X00000020;
        for(i=0;i<100000;i++);
        count++;
    }
     else {                                     /*turn off the leds on interrupt on secon press*/
         GPIOA->ODR &= 0X00000020;
         for(i=0;i<100000;i++);
         count--;
     }         
}

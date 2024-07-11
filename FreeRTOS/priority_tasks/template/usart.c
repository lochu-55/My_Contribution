#include "stm32f4xx.h"

void vApplicationIdleHook(void)
{
}

void usart_init() {
    RCC->AHB1ENR |= 0x00000001;
    RCC->APB1ENR |= 0x00020000;
   
    GPIOA->MODER &= ~(0x000000A0);
    GPIOA->MODER |= 0x000000A0;
   
    GPIOA->AFR[0] &= ~(0x00007700);
    GPIOA->AFR[0] |= 0x00007700;
   
    USART2->BRR |= 0x068B;
    USART2->CR1 |= 0x00000008;
    USART2->CR1 |= 0x00000040;
    USART2->CR1 |= 0x00002000;
}

int usart_getch() {
    while(!(USART2->SR & (0x00000020)));
    return ( (int) (USART2->DR & 0xFF));
}

void usart_putch(int ch) {
    while(!(USART2->SR & (0x00000080)));
    USART2->DR = (ch & 0x00FF);
}

int main() {
    int temp = 0;
    usart_init();

    usart_putch('h');
    usart_putch('e');
    usart_putch('l');
    usart_putch('l');
    usart_putch('0');

   
    while(1) {
        temp = usart_getch();
        usart_putch(temp);
    }
}

#include "stm32f4xx.h"

void USART2_Init(void);
void USART2_Write(char ch);
char USART2_Read(void);
void delayMs(int delay);

int main(void) {
    // Initialize USART2
    USART2_Init();
   
    // Send a welcome message
    char *msg = "Hello, UART!\r\n";
    while (*msg) {
        USART2_Write(*msg++);
    }
   
    while (1) {
        char c = USART2_Read(); // Read a character
        USART2_Write(c);        // Echo the character
    }
}

void USART2_Init(void) {
    // Enable clock for GPIOA and USART2
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;  // Enable GPIOA clock
    RCC->APB1ENR |= RCC_APB1ENR_USART2EN; // Enable USART2 clock
   
    // Configure PA2 as USART2_TX and PA3 as USART2_RX
    GPIOA->MODER &= ~((3 << 4) | (3 << 6)); // Clear mode bits for PA2, PA3
    GPIOA->MODER |= (2 << 4) | (2 << 6);    // Set mode bits to alternate function
    GPIOA->AFR[0] &= ~((0xF << 8) | (0xF << 12)); // Clear alternate function bits for PA2, PA3
    GPIOA->AFR[0] |= (7 << 8) | (7 << 12);  // Set alternate function to AF7 (USART2)
   
    // Configure USART2
    USART2->BRR = 0x0683;  // 9600 baud @ 16 MHz
    USART2->CR1 = USART_CR1_TE | USART_CR1_RE | USART_CR1_UE; // Enable TX, RX and USART2
}

void USART2_Write(char ch) {
    // Wait until the transmit data register is empty
    while (!(USART2->SR & USART_SR_TXE));
    // Write the data to the transmit data register
    USART2->DR = (ch & 0xFF);
}

char USART2_Read(void) {
    // Wait until the receive data register is not empty
    while (!(USART2->SR & USART_SR_RXNE));
    // Read the data from the receive data register
    return (char)(USART2->DR & 0xFF);
}

void delayMs(int delay) {
    int i;
    for (; delay > 0; delay--)
        for (i = 0; i < 3195; i++);
}

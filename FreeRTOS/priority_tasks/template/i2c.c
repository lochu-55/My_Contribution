#include "stm32f4xx.h"
#include <stdio.h>
#define I2C_EVENT_MASTER_MODE_SELECT              ((uint32_t)0x00030001)  /* BUSY, MSL and SB flag */
#define I2C_EVENT_MASTER_TRANSMITTER_MODE_SELECTED ((uint32_t)0x00070082)  /* BUSY, MSL, ADDR, TXE and TRA flags */
#define I2C_EVENT_MASTER_BYTE_TRANSMITTED         ((uint32_t)0x00070084)  /* TRA, BUSY, MSL, TXE and BTF flags*/
#define I2C_EVENT_MASTER_RECEIVER_MODE_SELECTED   ((uint32_t)0x00030002)  /* BUSY, MSL and ADDR flags */
#define I2C_EVENT_MASTER_BYTE_RECEIVED            ((uint32_t)0x00030040)  /* BUSY, MSL and RXNE flags */

void vApplicationIdleHook(void)
{
}

static const uint8_t TMP102_ADDR = 0x48 << 1; // 7-bit address shifted to the left
static const uint8_t REG_TEMP = 0x00;
float temperature_data;
uint8_t buf[2];
int16_t val;

uint32_t flag1;
uint32_t flag2;
uint32_t lastevent;

uint32_t func1(uint32_t I2C_EVENT) {
    uint32_t flag1 = I2C1->SR1;
    uint32_t flag2 = I2C1->SR2;
    flag2 = flag2 << 16;
    lastevent = (flag1 | flag2) & (uint32_t)0x00FFFFFF;
    return (lastevent == I2C_EVENT) ? 0 : 1;
}

void I2C_Config(void) {
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOBEN;
    RCC->APB1ENR |= RCC_APB1ENR_I2C1EN;

    GPIOB->MODER &= ~(GPIO_MODER_MODER8 | GPIO_MODER_MODER9);
    GPIOB->MODER |= (GPIO_MODER_MODER8_1 | GPIO_MODER_MODER9_1);

    GPIOB->OTYPER |= (GPIO_OTYPER_OT_8 | GPIO_OTYPER_OT_9);
    GPIOB->OSPEEDR |= (GPIO_OSPEEDER_OSPEEDR8 | GPIO_OSPEEDER_OSPEEDR9);
    GPIOB->PUPDR |= (GPIO_PUPDR_PUPDR8_0 | GPIO_PUPDR_PUPDR9_0);
    GPIOB->AFR[1] |= (4 << (4 * (8 - 8))) | (4 << (4 * (9 - 8))); // AF4 for I2C1 on PB8 and PB9

    I2C1->CR1 &= ~I2C_CR1_PE;
    I2C1->CR1 |= I2C_CR1_SWRST;
    I2C1->CR1 &= ~I2C_CR1_SWRST;

    I2C1->CR2 |= 0x10;
    I2C1->CCR = 80;
    I2C1->TRISE = 17;
    I2C1->CR1 |= I2C_CR1_PE;
}

void I2C_Write(void) {
    buf[0] = REG_TEMP;

    while(I2C1->SR2 & I2C_SR2_BUSY);
    I2C1->CR1 |= I2C_CR1_START;
    while (func1(I2C_EVENT_MASTER_MODE_SELECT));

    I2C1->DR = TMP102_ADDR;
    while (func1(I2C_EVENT_MASTER_TRANSMITTER_MODE_SELECTED));

    I2C1->DR = buf[0];
    while (func1(I2C_EVENT_MASTER_BYTE_TRANSMITTED));

    I2C1->CR1 |= I2C_CR1_STOP;
}

void I2C_Read(void) {
    while (I2C1->SR2 & I2C_SR2_BUSY);
    I2C1->CR1 |= I2C_CR1_START;
    while (func1(I2C_EVENT_MASTER_MODE_SELECT));

    I2C1->DR = TMP102_ADDR;
    while (func1(I2C_EVENT_MASTER_TRANSMITTER_MODE_SELECTED));

    I2C1->DR = REG_TEMP;
    while (func1(I2C_EVENT_MASTER_BYTE_TRANSMITTED));

    I2C1->CR1 |= I2C_CR1_START;
    while (func1(I2C_EVENT_MASTER_MODE_SELECT));

    I2C1->DR = TMP102_ADDR | 0x01;
    while (func1(I2C_EVENT_MASTER_RECEIVER_MODE_SELECTED));

    I2C1->CR1 |= I2C_CR1_ACK;
    while (func1(I2C_EVENT_MASTER_BYTE_RECEIVED));
    buf[0] = I2C1->DR;

    while (func1(I2C_EVENT_MASTER_BYTE_RECEIVED));
    buf[1] = I2C1->DR;

    I2C1->CR1 &= ~I2C_CR1_ACK;
    I2C1->CR1 |= I2C_CR1_STOP;

    val = ((int16_t)(buf[0] << 4) | (buf[1] >> 4));
    if (val > 0x7FF) {
        val |= 0xF000;
    }
    temperature_data = val * 0.0625;
}


void USART2_Init(void) {
    RCC->AHB1ENR |= 0x00000001;  // Enable GPIOA clock
    RCC->APB1ENR |= 0x00020000;  // Enable USART2 clock

    GPIOA->MODER &= ~(0x00000F00);
    GPIOA->MODER |= 0x00000A00;

    GPIOA->AFR[0] &= ~(0xFF00);
    GPIOA->AFR[0] |= 0x7700;

    USART2->BRR = 0x0683;  // 9600 baud @ 16 MHz
    USART2->CR1 |= 0x0008; // Enable transmitter
    USART2->CR1 |= 0x2000; // Enable USART
}

void USART2_Write(char ch) {
    while (!(USART2->SR & 0x0080));
    USART2->DR = (ch & 0xFF);
}

void USART2_WriteString(const char *str) {
    while (*str) {
        USART2_Write(*str++);
    }
}

int main(void) {
    I2C_Config();
    USART2_Init();
    I2C_Write();
    I2C_Read();

    char buffer[50];
    snprintf(buffer, sizeof(buffer), "Temperature: %.2f C\r\n", temperature_data);
    USART2_WriteString(buffer);

    while (1) {
        // Loop forever
    }
}

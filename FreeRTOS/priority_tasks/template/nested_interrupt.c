#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include "stm32f4xx.h"
#include <stdio.h>
#include <stdarg.h>

#define LOW_PRIORITY_IRQn  EXTI15_10_IRQn
#define HIGH_PRIORITY_IRQn EXTI0_IRQn

QueueHandle_t xQueue;

void vPrintString(const char *format, ...);

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

void vApplicationIdleHook(void) {
    // Idle hook function
}

// High priority interrupt handler
void EXTI0_IRQHandler(void) {
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    const char *message = "High priority interrupt triggered.\r\n";

    if (EXTI->PR & EXTI_PR_PR0) {
        EXTI->PR = EXTI_PR_PR0; // Clear the interrupt flag

        vPrintString("High priority interrupt triggered.\r\n");

        // Send a message to the queue from the ISR
        xQueueSendFromISR(xQueue, &message, &xHigherPriorityTaskWoken);

        // Optionally, yield if a higher priority task was woken
        portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
    }
}

// Low priority interrupt handler
void EXTI15_10_IRQHandler(void) {
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    const char *message = "Low priority interrupt triggered.\r\n";

    if (EXTI->PR & EXTI_PR_PR10) {
        EXTI->PR = EXTI_PR_PR10; // Clear the interrupt flag

        vPrintString("Low priority interrupt triggered.\r\n");

        // Send a message to the queue from the ISR
        xQueueSendFromISR(xQueue, &message, &xHigherPriorityTaskWoken);

        // Trigger high priority interrupt from within the low priority interrupt
        NVIC_SetPendingIRQ(HIGH_PRIORITY_IRQn);

        // Optionally, yield if a higher priority task was woken
        portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
    }
}

// Task to print messages received from the queue
void vPrintTask(void *pvParameters) {
    char *message;

    for (;;) {
        // Wait for a message to arrive in the queue
        if (xQueueReceive(xQueue, &message, portMAX_DELAY) == pdPASS) {
            // Print the message
            vPrintString("%s", message);
        }
    }
}

// Function to configure EXTI lines
void configureEXTILines(void) {
    // Enable GPIOC clock
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOCEN;

    // Configure PC0 and PC10 as input
    GPIOC->MODER &= ~(GPIO_MODER_MODER0 | GPIO_MODER_MODER10);

    // Enable SYSCFG clock
    RCC->APB2ENR |= RCC_APB2ENR_SYSCFGEN;

    // Connect EXTI0 line to PC0
    SYSCFG->EXTICR[0] &= ~SYSCFG_EXTICR1_EXTI0;
    SYSCFG->EXTICR[0] |= SYSCFG_EXTICR1_EXTI0_PC;

    // Connect EXTI10 line to PC10
    SYSCFG->EXTICR[2] &= ~SYSCFG_EXTICR3_EXTI10;
    SYSCFG->EXTICR[2] |= SYSCFG_EXTICR3_EXTI10_PC;

    // Configure EXTI0 and EXTI10 for rising edge trigger
    EXTI->RTSR |= EXTI_RTSR_TR0 | EXTI_RTSR_TR10;

    // Enable EXTI0 and EXTI10
    EXTI->IMR |= EXTI_IMR_MR0 | EXTI_IMR_MR10;

    // Clear any pending interrupt
    EXTI->PR = EXTI_PR_PR0 | EXTI_PR_PR10;
}

// Main function
int main(void) {
    // Initialize the hardware
    SystemInit();

    // Configure EXTI lines
    configureEXTILines();

    // Initialize the queue
    xQueue = xQueueCreate(10, sizeof(char *));
    if (xQueue == NULL) {
        vPrintString("Failed to create queue.\r\n");
        while (1);
    }

    // Create the print task
    if (xTaskCreate(vPrintTask, "PrintTask", configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 1, NULL) != pdPASS) {
        vPrintString("Failed to create task.\r\n");
        while (1);
    }

    // Configure the interrupt priority and enable the interrupts
    NVIC_SetPriority(LOW_PRIORITY_IRQn, 5); // Directly set priority to 5
    NVIC_SetPriority(HIGH_PRIORITY_IRQn, 4); // Directly set priority to 4
    NVIC_EnableIRQ(LOW_PRIORITY_IRQn);
    NVIC_EnableIRQ(HIGH_PRIORITY_IRQn);

    // Start the scheduler
    vTaskStartScheduler();

    // The following line should never be reached
    for (;;);
}

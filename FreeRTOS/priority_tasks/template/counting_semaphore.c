#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <stdio.h>
#include <stdarg.h>

/* Declare a counting semaphore handle */
SemaphoreHandle_t xCountingSemaphore;
void vApplicationIdleHook(void)
{
}
/* Utility function to print to console */
void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

/* Task function that handles the software interrupt */
void vHandlerTask(void *pvParameters) {
    for (;;) {
        /* Wait indefinitely for the semaphore */
        if (xSemaphoreTake(xCountingSemaphore, portMAX_DELAY) == pdTRUE) {
            vPrintString("Handler task - Processing event.\r\n");
        }
    }
}

/* Function to simulate raising an interrupt */
void vRaiseInterrupt(void) {
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    /* Print ISR message */
    vPrintString("Simulated ISR: Giving semaphore.\r\n");

    /* Give the semaphore to unblock the handler task */
    xSemaphoreGiveFromISR(xCountingSemaphore, &xHigherPriorityTaskWoken);
    xSemaphoreGiveFromISR(xCountingSemaphore, &xHigherPriorityTaskWoken);
    xSemaphoreGiveFromISR(xCountingSemaphore, &xHigherPriorityTaskWoken);

    /* Perform a context switch if necessary */
    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
}

/* Task function that periodically generates an interrupt */
void vPeriodicTask(void *pvParameters) {
    const TickType_t xDelay500ms = pdMS_TO_TICKS(500UL);

    /* As per most tasks, this task is implemented within an infinite loop. */
    for (;;) {
        /* Print message indicating intent to generate an interrupt */
        vPrintString("Periodic task - About to generate an interrupt.\r\n");

        /* Simulate raising an interrupt */
        vRaiseInterrupt();

        /* Print message indicating interrupt generation */
        vPrintString("Periodic task - Interrupt generated.\r\n\n");

        /* Block until it is time to generate the interrupt again. */
        vTaskDelay(xDelay500ms);
    }
}

/* Main function */
int main(void) {
    /* Before a semaphore is used it must be explicitly created */
    xCountingSemaphore = xSemaphoreCreateCounting(10, 0);

    /* Check the semaphore was created successfully */
    if (xCountingSemaphore != NULL) {
        /* Create the handler task */
        xTaskCreate(vHandlerTask, "Handler", configMINIMAL_STACK_SIZE, NULL, 2, NULL);

        /* Create the periodic task */
        xTaskCreate(vPeriodicTask, "Periodic", configMINIMAL_STACK_SIZE, NULL, 1, NULL);

        /* Start the FreeRTOS scheduler */
        vTaskStartScheduler();
    }

    /* The following line should never be reached */
    for (;;);
}

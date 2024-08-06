#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <stdio.h>
#include <stdarg.h>

/* Declare a binary semaphore handle */
SemaphoreHandle_t xBinarySemaphore;

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

/* Task function that periodically generates a software interrupt */
void vPeriodicTask(void *pvParameters) {
    const TickType_t xDelay500ms = pdMS_TO_TICKS(500UL);

    for (;;) {
        /* Block until it is time to generate the software interrupt again */
        vTaskDelay(xDelay500ms);

        vPrintString("Periodic task - About to generate an interrupt.\r\n");

        /* Simulate an interrupt handling by giving the semaphore */
        if (xSemaphoreGive(xBinarySemaphore) != pdTRUE) {
            vPrintString("Failed to give semaphore.\r\n");
        }

        vPrintString("Periodic task - Interrupt generated.\r\n\r\n\r\n");
    }
}

/* Task function that handles the software interrupt */
void vHandlerTask(void *pvParameters) {
    for (;;) {
        /* Wait indefinitely for the semaphore */
        if (xSemaphoreTake(xBinarySemaphore, portMAX_DELAY) == pdTRUE) {
            vPrintString("Handler task - Processing event.\r\n");
        }
    }
}

/* Main function */
int main(void) {
    /* Before a semaphore is used it must be explicitly created */
    xBinarySemaphore = xSemaphoreCreateBinary();

    /* Check the semaphore was created successfully */
    if (xBinarySemaphore != NULL) {
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

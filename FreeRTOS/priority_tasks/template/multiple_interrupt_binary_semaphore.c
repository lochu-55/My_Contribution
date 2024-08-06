#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <stdio.h>
#include <stdarg.h>

/* Declare a binary semaphore handle */
SemaphoreHandle_t xBinarySemaphore;
volatile uint32_t ulInterruptCount = 0;
static uint32_t taskCount = 0;

void vApplicationIdleHook(void)
{
}
/* Function prototypes */
void vMyTask(void *pvParameters);
void vPeriodicInterruptGenerator(void *pvParameters);

/* Utility function to print to console */
void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

/* Task function that waits for the binary semaphore */
void vMyTask(void *pvParameters) {
    for (;;) {
        /* Wait for the semaphore to be given by the ISR */
        if (xSemaphoreTake(xBinarySemaphore, portMAX_DELAY) == pdTRUE) {
            vPrintString("Task: Processing interrupt event.\r\n");
            taskCount = ulInterruptCount;
            /* Simulate some processing time */
            vTaskDelay(pdMS_TO_TICKS(500));

            vPrintString("Task: Finished processing event.%lu\r\n",taskCount);
        }
    }
}

/* Simulated ISR Handler */
void vMyISRHandler(void) {
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    /* Give the semaphore to unblock the task */
    xSemaphoreGiveFromISR(xBinarySemaphore, &xHigherPriorityTaskWoken);

    /* Request a context switch if a higher priority task was unblocked */
    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
    ulInterruptCount++;
    vPrintString("Simulated ISR: Interrupt number %lu.\r\n", ulInterruptCount);
}

/* Task to simulate periodic interrupts */
void vPeriodicInterruptGenerator(void *pvParameters) {
    const TickType_t xDelay = pdMS_TO_TICKS(200); // 200 ms delay to simulate high frequency interrupts

    for (;;) {
        vTaskDelay(xDelay);
        vPrintString("Simulated ISR: Giving semaphore.\r\n");
        vMyISRHandler();
    }
}

/* Main function */
int main(void) {
    /* Create the binary semaphore */
    xBinarySemaphore = xSemaphoreCreateBinary();

    /* Ensure the semaphore was created successfully */
    if (xBinarySemaphore != NULL) {
        /* Create the task that will wait for the semaphore */
        xTaskCreate(vMyTask, "MyTask", configMINIMAL_STACK_SIZE, NULL, 1, NULL);

        /* Create the task that will simulate periodic interrupts */
        xTaskCreate(vPeriodicInterruptGenerator, "InterruptGenerator", configMINIMAL_STACK_SIZE, NULL, 2, NULL);

        /* Start the scheduler */
        vTaskStartScheduler();
    }

    /* The following line should never be reached */
    for (;;) {
    }

}

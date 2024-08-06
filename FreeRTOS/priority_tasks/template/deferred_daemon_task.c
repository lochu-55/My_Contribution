#include "FreeRTOS.h"
#include "task.h"
#include "timers.h"
#include <stdio.h>
#include <stdarg.h>

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


/* Deferred handling function */
void vDeferredHandlingFunction(void *pvParameter1, uint32_t ulParameter2) {
    /* Process the event - in this case just print out a message and the value of ulParameter2 */
    vPrintString("Handler function - Processing event %lu\r\n", ulParameter2);
}



/* Example interrupt handler */
static uint32_t ulExampleInterruptHandler(void) {
    static uint32_t ulParameterValue = 0;
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    xTimerPendFunctionCallFromISR(vDeferredHandlingFunction, /* Function to execute. */
                                  NULL,                      /* Not used. */
                                  ulParameterValue,          /* Incrementing value. */
                                  &xHigherPriorityTaskWoken);
    ulParameterValue++;

    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
}



/* Function to simulate raising an interrupt */
void vRaiseInterrupt(void) {
    /* Print ISR message */
    vPrintString("Simulated ISR: Triggering example interrupt.\r\n");

    /* Simulate an interrupt by directly calling the handler */
    ulExampleInterruptHandler();
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
        vPrintString("Periodic task - Interrupt generated.\r\n");

        /* Block until it is time to generate the interrupt again. */
        vTaskDelay(xDelay500ms);
    }
}

/* Main function */
int main(void) {
    /* The priority of the daemon task is set by the configTIMER_TASK_PRIORITY compile time configuration constant in FreeRTOSConfig.h. */
    const UBaseType_t ulPeriodicTaskPriority = configTIMER_TASK_PRIORITY - 1;

    /* Create the task that will periodically generate a software interrupt. */
    xTaskCreate(vPeriodicTask, "Periodic", configMINIMAL_STACK_SIZE, NULL, ulPeriodicTaskPriority, NULL);

    /* Start the FreeRTOS scheduler */
    vTaskStartScheduler();

    /* The following line should never be reached */
    for (;;);
}

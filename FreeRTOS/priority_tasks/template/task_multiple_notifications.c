#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>
#include <stdarg.h>

/* Function prototypes */
static void vPeriodicTask(void *pvParameters);
static void vHandlerTask(void *pvParameters);
static uint32_t ulExampleInterruptHandler(void);
const TickType_t xInterruptFrequency = pdMS_TO_TICKS( 500UL );

/* Define the handler task handle */
TaskHandle_t xHandlerTask = NULL;

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

void vApplicationIdleHook(void) { }

/* Main function */
int main(void) {
    /* Create the 'handler' task, which is the task to which interrupt processing is deferred */
    xTaskCreate(vHandlerTask, "Handler", configMINIMAL_STACK_SIZE, NULL, 3, &xHandlerTask);

    /* Create the task that will periodically generate a software interrupt */
    xTaskCreate(vPeriodicTask, "Periodic", configMINIMAL_STACK_SIZE, NULL, 1, NULL);

    /* Start the scheduler */
    vTaskStartScheduler();

    /* As normal, the following line should never be reached */
    for (;;) {
    }
}

/* Periodic task function */
static void vPeriodicTask(void *pvParameters) {
    const TickType_t xDelay250ms = pdMS_TO_TICKS(1000UL); // Shorter delay

    /* Infinite loop */
    for (;;) {
        /* Print a message before generating the "interrupt" */
        vPrintString("Periodic task - About to generate an interrupt.\r\n");

        /* Block until it is time to generate the "interrupt" again */
        vTaskDelay(xDelay250ms); // Shorter delay

        /* Generate the "interrupt" */
        ulExampleInterruptHandler();
        /* Print a message after generating the "interrupt" */
        vPrintString("Periodic task - Interrupt generated.\r\n\r\n\r\n");
    }
}

/* Handler task function */
static void vHandlerTask(void *pvParameters) {
    const TickType_t xMaxExpectedBlockTime = xInterruptFrequency + pdMS_TO_TICKS( 100 ); // Longer delay
    uint32_t ulEventsToProcess;

    /* Infinite loop */
    for (;;) {
        /* Wait to receive a notification sent directly to this task from the interrupt service routine */
        ulEventsToProcess = ulTaskNotifyTake(pdFALSE, xMaxExpectedBlockTime);

    

        /* Check if events were received */
        if (ulEventsToProcess != 0) {
            /* Process each event */
                vPrintString("Handler task - Processing event.\r\n");
        
        } else {
            /* Handle error recovery operations if an interrupt did not arrive within the expected time */
        }

    }
}


/* Interrupt handler function */
static uint32_t ulExampleInterruptHandler(void) {
     BaseType_t xHigherPriorityTaskWoken;
     xHigherPriorityTaskWoken = pdFALSE;
     /* Send a notification to the handler task multiple times. The first ‘give’ will
     unblock the task, the following 'gives' are to demonstrate that the receiving 
     task's notification value is being used to count (latch) events - allowing the 
     task to process each event in turn. */
     vTaskNotifyGiveFromISR( xHandlerTask, &xHigherPriorityTaskWoken );
     vTaskNotifyGiveFromISR( xHandlerTask, &xHigherPriorityTaskWoken );
     vTaskNotifyGiveFromISR( xHandlerTask, &xHigherPriorityTaskWoken );
     portYIELD_FROM_ISR( xHigherPriorityTaskWoken );
    return 0;
}

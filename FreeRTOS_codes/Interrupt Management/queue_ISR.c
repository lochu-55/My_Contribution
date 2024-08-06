#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include "timers.h"
#include <stdio.h>
#include <stdarg.h>

// Define the queue handles globally
static QueueHandle_t xIntegerQueue = NULL;
static QueueHandle_t xStringQueue = NULL;


// Print utility function
void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

// Idle hook function
void vApplicationIdleHook(void) {
    // Idle hook code here
}

// Deferred handling function
void vDeferredHandlingFunction(void *pvParameter1, uint32_t ulParameter2) {
    vPrintString("Handler function - Processing event %lu\r\n", ulParameter2);
}

// Example interrupt handler
static uint32_t ulExampleInterruptHandler(void) {
    BaseType_t xHigherPriorityTaskWoken;
    uint32_t ulReceivedNumber;
    static const char *pcStrings[] = {
        "String 0\r\n",
        "String 1\r\n",
        "String 2\r\n",
        "String 3\r\n"
    };
    xHigherPriorityTaskWoken = pdFALSE;

    // Read from the queue until the queue is empty
    while (xQueueReceiveFromISR(xIntegerQueue, &ulReceivedNumber, &xHigherPriorityTaskWoken) != errQUEUE_EMPTY) {
        ulReceivedNumber &= 0x03;
        xQueueSendToBackFromISR(xStringQueue, &pcStrings[ulReceivedNumber], &xHigherPriorityTaskWoken);
    }

    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
    return 0;  // Return value not used in this context
}

// Function to simulate raising an interrupt
void vRaiseInterrupt(void) {
    vPrintString("Simulated ISR: Triggering example interrupt.\r\n");
    ulExampleInterruptHandler();
}


// Integer generator task
static void vIntegerGenerator(void *pvParameters) {
    TickType_t xLastExecutionTime;
    uint32_t ulValueToSend = 0;
    int i;
    xLastExecutionTime = xTaskGetTickCount();

    for (;;) {
        vTaskDelayUntil(&xLastExecutionTime, pdMS_TO_TICKS(200));

        for (i = 0; i < 5; i++) {
            xQueueSendToBack(xIntegerQueue, &ulValueToSend, 0);
            ulValueToSend++;
        }

        vPrintString("Generator task - About to generate an interrupt.\r\n");
        vRaiseInterrupt();
        vPrintString("Generator task - Interrupt generated.\r\n\r\n\r\n");
    }
}

// String printer task
static void vStringPrinter(void *pvParameters) {
    char *pcString;

    for (;;) {
        xQueueReceive(xStringQueue, &pcString, portMAX_DELAY);
        vPrintString(pcString);
    }
}

int main(void) {
    xIntegerQueue = xQueueCreate(10, sizeof(uint32_t));
    xStringQueue = xQueueCreate(10, sizeof(char *));
    
    if (xIntegerQueue == NULL || xStringQueue == NULL) {
        vPrintString("Failed to create queues\r\n");
    }
    
    xTaskCreate(vIntegerGenerator, "IntGen", configMINIMAL_STACK_SIZE, NULL, 1, NULL);
    xTaskCreate(vStringPrinter, "String", configMINIMAL_STACK_SIZE, NULL, 2, NULL);

    // Note: vPortSetInterruptHandler is specific to FreeRTOS Windows port. 
    // For actual MCU, ensure the proper interrupt setup.
    // vPortSetInterruptHandler(mainINTERRUPT_NUMBER, ulExampleInterruptHandler);

    vTaskStartScheduler();

    for (;;);
}

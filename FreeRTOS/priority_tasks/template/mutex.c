#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

// Mutex handle
SemaphoreHandle_t xMutex;

void vApplicationIdleHook(void) {
    // Idle hook implementation (optional)
}

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

void prvNewPrintString(const char *pcString) {
    // Attempt to take the mutex, blocking indefinitely if it's not available
    if (xSemaphoreTake(xMutex, portMAX_DELAY) == pdTRUE) {
        // The following line will only execute once the mutex has been successfully obtained
        vPrintString("%s", pcString);
        vTaskDelay(1000);
        fflush(stdout); // Ensure output is flushed
        
        // The mutex MUST be given back!
        xSemaphoreGive(xMutex);
    } else {
        // Failed to take the mutex
        vPrintString("Failed to take the mutex\n");
    }
}

void prvPrintTask(void *pvParameters) {
    const char *pcStringToPrint;
    const TickType_t xMaxBlockTimeTicks = 0x20;
    
    // The string to print is passed as the task's parameter
    pcStringToPrint = (const char *)pvParameters;
    
    for(;;) {
        // Print out the string using the newly defined function
        prvNewPrintString(pcStringToPrint);
        
        // Wait a pseudo-random time
        vTaskDelay((rand() % xMaxBlockTimeTicks));
    }
}

int main(void) {
    // Initialize the mutex before the scheduler is started
    xMutex = xSemaphoreCreateMutex();
    
    // Check the mutex was created successfully before creating the tasks
    if (xMutex != NULL) {
        vPrintString("Mutex created successfully\n");
        
        // Create two instances of the tasks that write to stdout
        if (xTaskCreate(prvPrintTask, "Print1", 130, "Task 1 ***************************************\n", 1, NULL) == pdPASS) {
            vPrintString("Task 1 created successfully\n");
        } else {
            vPrintString("Failed to create Task 1\n");
        }
        
        if (xTaskCreate(prvPrintTask, "Print2", 130, "Task 2 ---------------------------------------\n", 2, NULL) == pdPASS) {
            vPrintString("Task 2 created successfully\n");
        } else {
            vPrintString("Failed to create Task 2\n");
        }
        
        // Start the scheduler so the created tasks start executing
        vTaskStartScheduler();
    } else {
        vPrintString("Mutex not created successfully\n");
    }
    
    // If all is well, main() will never reach here
    for(;;);
}

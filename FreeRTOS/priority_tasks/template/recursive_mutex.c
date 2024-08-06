#include <stdio.h>
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

// Define task priorities
#define TASK1_PRIORITY   (configMAX_PRIORITIES )

// Define task handles
TaskHandle_t task1Handle;

// Define a recursive mutex
SemaphoreHandle_t recursiveMutex;

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

void vApplicationIdleHook(void) {
        //vPrintString("idle...");
}

// Function 1
void function1(void) {
    vPrintString("Function1 trying to acquire recursive mutex\n");
    if (xSemaphoreTakeRecursive(recursiveMutex, portMAX_DELAY) == pdTRUE) {
        vPrintString("Function1 acquired recursive mutex\n");
        // Perform some task
        xSemaphoreGiveRecursive(recursiveMutex);
        vPrintString("Function1 released recursive mutex\n");
    }
}

// Task 1
void vTask1(void *pvParameters) {
    while(1) {
        vPrintString("Task 1 trying to acquire recursive mutex\n");
        if (xSemaphoreTakeRecursive(recursiveMutex, portMAX_DELAY) == pdTRUE) {
            vPrintString("Task 1 acquired recursive mutex\n");

            // Nested function call acquiring the same mutex
            vPrintString("Task 1 calling function1()\n");
            function1();

            xSemaphoreGiveRecursive(recursiveMutex);
            vPrintString("Task 1 released recursive mutex\n");
        }
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay for 1 second
    }
}



int main() {
    // Create a recursive mutex
    recursiveMutex = xSemaphoreCreateRecursiveMutex();

    // Create task
    xTaskCreate(vTask1, "Task1", configMINIMAL_STACK_SIZE, NULL, TASK1_PRIORITY, &task1Handle);

    // Start scheduler
    vTaskStartScheduler();

    for(;;);
    
}

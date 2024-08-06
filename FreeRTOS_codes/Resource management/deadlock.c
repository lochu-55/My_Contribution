#include <stdio.h>
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

// Define task priorities
#define TASK1_PRIORITY   (configMAX_PRIORITIES )
#define TASK2_PRIORITY   (configMAX_PRIORITIES - 1)
#define WATCHDOG_PRIORITY (configMAX_PRIORITIES - 2)

// Define task handles
TaskHandle_t task1Handle;
TaskHandle_t task2Handle;

// Define mutexes
SemaphoreHandle_t mutex1;
SemaphoreHandle_t mutex2;

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

const char* getTaskStateString(eTaskState state) {
    switch (state) {
        case eRunning:   return "Running";
        case eReady:     return "Ready";
        case eBlocked:   return "Blocked";
        case eSuspended: return "Suspended";
        case eDeleted:   return "Deleted";
        default:         return "Unknown";
    }
}

// Function to print deadlock condition
void printDeadlockCondition(void) {
    vPrintString("Deadlock Condition Detected:\n");
    vPrintString("Task 1 status: %s\n", getTaskStateString(eTaskGetState(task1Handle)));
    vPrintString("Task 2 status: %s\n", getTaskStateString(eTaskGetState(task2Handle)));
    vPrintString("Mutex 1 count: %d\n", (int)uxSemaphoreGetCount(mutex1));
    vPrintString("Mutex 2 count: %d\n", (int)uxSemaphoreGetCount(mutex2));
}

// Watchdog task to detect deadlocks
void vWatchdogTask(void *pvParameters) {
    while(1) {
        // Check if both tasks are blocked
        if ((eTaskGetState(task1Handle) == eBlocked) && (eTaskGetState(task2Handle) == eBlocked)) {
            printDeadlockCondition();
        }
        vTaskDelay(pdMS_TO_TICKS(1000)); // Check every second
    }
}

// Task 1
void vTask1(void *pvParameters) {
    while(1) {
        printf("Task 1 trying to acquire mutex 1\n");
        if (xSemaphoreTake(mutex1, portMAX_DELAY) == pdTRUE) {
            printf("Task 1 acquired mutex 1\n");
            vTaskDelay(pdMS_TO_TICKS(500)); // Simulate work
            printf("Task 1 trying to acquire mutex 2\n");
            if (xSemaphoreTake(mutex2, portMAX_DELAY) == pdTRUE) {
                printf("Task 1 acquired mutex 2\n");
                // Do something with mutex 1 and mutex 2...
                xSemaphoreGive(mutex2);
                printf("Task 1 released mutex 2\n");
            } else {
                // Print deadlock condition if unable to acquire mutex 2
                printDeadlockCondition();
            }
            xSemaphoreGive(mutex1);
            printf("Task 1 released mutex 1\n");
        } else {
            // Print deadlock condition if unable to acquire mutex 1
            printDeadlockCondition();
        }
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

// Task 2
void vTask2(void *pvParameters) {
    while(1) {
        printf("Task 2 trying to acquire mutex 2\n");
        if (xSemaphoreTake(mutex2, portMAX_DELAY) == pdTRUE) {
            printf("Task 2 acquired mutex 2\n");
            vTaskDelay(pdMS_TO_TICKS(500)); // Simulate work
            printf("Task 2 trying to acquire mutex 1\n");
            if (xSemaphoreTake(mutex1, portMAX_DELAY) == pdTRUE) {
                printf("Task 2 acquired mutex 1\n");
                // Do something with mutex 1 and mutex 2...
                xSemaphoreGive(mutex1);
                printf("Task 2 released mutex 1\n");
            } else {
                // Print deadlock condition if unable to acquire mutex 1
                printDeadlockCondition();
            }
            xSemaphoreGive(mutex2);
            printf("Task 2 released mutex 2\n");
        } else {
            // Print deadlock condition if unable to acquire mutex 2
            printDeadlockCondition();
        }
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

int main() {
    // Create mutexes
    mutex1 = xSemaphoreCreateMutex();
    mutex2 = xSemaphoreCreateMutex();

    // Create tasks
    xTaskCreate(vTask1, "Task1", configMINIMAL_STACK_SIZE, NULL, TASK1_PRIORITY, &task1Handle);
    xTaskCreate(vTask2, "Task2", configMINIMAL_STACK_SIZE, NULL, TASK2_PRIORITY, &task2Handle);
    xTaskCreate(vWatchdogTask, "Watchdog", configMINIMAL_STACK_SIZE, NULL, WATCHDOG_PRIORITY, NULL);

    // Start scheduler
    vTaskStartScheduler();

    for(;;);
}

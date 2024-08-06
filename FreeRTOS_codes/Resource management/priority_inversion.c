#include <stdio.h>
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

// Define task priorities
#define HIGH_PRIORITY   (configMAX_PRIORITIES - 1)
#define MEDIUM_PRIORITY (configMAX_PRIORITIES - 2)
#define LOW_PRIORITY    (configMAX_PRIORITIES - 3)


// Define task handles
TaskHandle_t highTaskHandle;
TaskHandle_t mediumTaskHandle;
TaskHandle_t lowTaskHandle;

// Define a mutex (resource)
SemaphoreHandle_t mutex;


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

// High priority task
void vHighPriorityTask(void *pvParameters) {
    while(1) {
        vPrintString("High priority task trying to acquire mutex\n");
        if (xSemaphoreTake(mutex, portMAX_DELAY) == pdTRUE) {
            printf("High priority task acquired mutex\n");
            // Simulate some work
            vTaskDelay(pdMS_TO_TICKS(1000));
            xSemaphoreGive(mutex);
            printf("High priority task released mutex\n");
        }
        vTaskDelay(pdMS_TO_TICKS(2000));
    }
}

// Medium priority task
void vMediumPriorityTask(void *pvParameters) {
    while(1) {
        vPrintString("Medium priority task trying to acquire mutex\n");
        if (xSemaphoreTake(mutex, portMAX_DELAY) == pdTRUE) {
            vPrintString("Medium priority task acquired mutex\n");
            // Simulate some work
            vTaskDelay(pdMS_TO_TICKS(500));
            vPrintString("Medium priority task releasing mutex\n");
            xSemaphoreGive(mutex);
        }
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

// Low priority task
void vLowPriorityTask(void *pvParameters) {
    while(1) {
        vPrintString("Low priority task trying to acquire mutex\n");
        if (xSemaphoreTake(mutex, portMAX_DELAY) == pdTRUE) {
            vPrintString("Low priority task acquired mutex\n");
            // Simulate some work
            vTaskDelay(pdMS_TO_TICKS(200));
            xSemaphoreGive(mutex);
            vPrintString("Low priority task released mutex\n");
        }
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

int main() {
    // Create mutex
    mutex = xSemaphoreCreateMutex();

    // Create tasks
    xTaskCreate(vHighPriorityTask, "High", configMINIMAL_STACK_SIZE, NULL, HIGH_PRIORITY, &highTaskHandle);
    xTaskCreate(vMediumPriorityTask, "Medium", configMINIMAL_STACK_SIZE, NULL, MEDIUM_PRIORITY, &mediumTaskHandle);
    xTaskCreate(vLowPriorityTask, "Low", configMINIMAL_STACK_SIZE, NULL, LOW_PRIORITY, &lowTaskHandle);

    // Start scheduler
    vTaskStartScheduler();
    for(;;);
}

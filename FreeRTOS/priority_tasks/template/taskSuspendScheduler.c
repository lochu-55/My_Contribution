#include "FreeRTOS.h"  // Include FreeRTOS header for fundamental FreeRTOS definitions
#include "task.h"      // Include task header for task management functions
#include <stdio.h>     // Include standard I/O header for printf

// Task handles
TaskHandle_t TaskA_Handle;
TaskHandle_t TaskB_Handle;

// Shared resource
volatile int sharedResource = 1;

// Task function prototypes
void TaskA(void *pvParameters);
void TaskB(void *pvParameters);

int main(void) {
    // Create Task A
    xTaskCreate(TaskA, "TaskA", configMINIMAL_STACK_SIZE, NULL, 1, &TaskA_Handle);

    // Create Task B
    xTaskCreate(TaskB, "TaskB", configMINIMAL_STACK_SIZE, NULL, 1, &TaskB_Handle);

    // Start FreeRTOS scheduler
    vTaskStartScheduler();
    for(;;);
}



void TaskA(void *pvParameters) {
    while (1) {
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay for 1 second
        
        // Enter critical section using vTaskSuspendScheduler()
        vTaskSuspendAll();

        // Access shared resource
        sharedResource++;
        printf("Task A: Incremented shared resource to %d\n", sharedResource);

        // Exit critical section
        xTaskResumeAll();
    }
}

void TaskB(void *pvParameters) {
    while (1) {
        vTaskDelay(pdMS_TO_TICKS(1000)); // Delay for 1.5 seconds
        
        // Enter global critical section using vTaskSuspendAll()
        vTaskSuspendAll();

        // Access shared resource
        sharedResource--;
        printf("Task B: Decremented shared resource to %d\n", sharedResource);

        // Exit global critical section
        xTaskResumeAll();
    }
}

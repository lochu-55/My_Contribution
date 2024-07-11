#include "FreeRTOS.h"
#include "task.h"
#include "portable.h"
#include <stdio.h>

// Define the memory regions that will be used for the heap. These regions should be contiguous blocks of memory.
static uint8_t ucHeap1[1024];
static uint8_t ucHeap2[2048];
static uint8_t ucHeap3[4096];

// Define an array of HeapRegion_t structures to specify the start addresses and sizes of the memory regions.
HeapRegion_t xHeapRegions[] = {
    { ucHeap1, sizeof(ucHeap1) },  // Region 1
    { ucHeap2, sizeof(ucHeap2) },  // Region 2
    { ucHeap3, sizeof(ucHeap3) },  // Region 3
    { NULL, 0 }                    // Terminator
};

// Example task function
void vExampleTask(void *pvParameters) {
    for (;;) {
        // Task code goes here.
        vTaskDelay(pdMS_TO_TICKS(1000));  // Delay for 1000 ms
    }
}

int main(void) {
    // Configure the heap regions
    vPortDefineHeapRegions(xHeapRegions);

    // Create example tasks
    xTaskCreate(vExampleTask, "Task1", configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 1, NULL);

    // Start the scheduler
    vTaskStartScheduler();

    // The code should never reach here unless there's insufficient heap available to start the scheduler
    for (;;);
}

void vApplicationMallocFailedHook(void) {
    // Malloc failed hook implementation
    printf("Malloc failed!\n");
    for (;;);
}

void vApplicationStackOverflowHook(TaskHandle_t xTask, char *pcTaskName) {
    // Stack overflow hook implementation
    printf("Stack overflow in task: %s\n", pcTaskName);
    for (;;);
}
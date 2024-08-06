#include <stdio.h>
#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include "heap_utils.h"

void vApplicationIdleHook(void)
{
}



// Task that prints the free heap size
void vFreeHeapSizeTask(void *pvParameters) {
    size_t freeHeapSize;
    for (;;) {
        freeHeapSize = xPortGetFreeHeapSize();
        printf("Free Heap Size: %u bytes\n", (unsigned int)freeHeapSize);
        vTaskDelay(pdMS_TO_TICKS(1000));  // Delay for 1000 ms
    }
}


void vMinEverFreeHeapSizeTask(void *pvParameters) {
    size_t minEverFreeHeapSize;
    for (;;) {
        minEverFreeHeapSize = xPortGetMinimumEverFreeHeapSize();
        printf("Min Ever Free Heap Size: %u bytes\n", (unsigned int)minEverFreeHeapSize);
        vTaskDelay(pdMS_TO_TICKS(1000));  // Delay for 1000 ms
    }
}


int main(void) {
    // Create tasks
    xTaskCreate(vFreeHeapSizeTask, "FreeHeapTask", configMINIMAL_STACK_SIZE, NULL,1, NULL);
    xTaskCreate(vMinEverFreeHeapSizeTask, "MinEverFreeHeapTask", configMINIMAL_STACK_SIZE, NULL,1, NULL);
    // Start the scheduler
    vTaskStartScheduler();

    // The code should never reach here unless there's insufficient heap available to start the scheduler
    for (;;);
}

#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include <stdio.h>

// Queue handle
QueueHandle_t xNumberQueue;
void vApplicationIdleHook(void) {
    // Idle hook implementation (optional)
}
// Task parameters
#define QUEUE_LENGTH    5

// Task to send numbers to the queue
void vSenderTask(void *pvParameters) {
    TickType_t xLastWakeTime = xTaskGetTickCount();
    int numbers[] = {1, 2, 3, 4, 5};
    int index = 0;

    for (;;) {
        // Attempt to send number to queue, overwriting third number if queue is full
        if (xQueueSendToBack(xNumberQueue, &numbers[index], 0) == pdTRUE) {
            printf("Sent to queue: %d\n", numbers[index]);
        } else {
            // Queue is full, overwrite the third number
            int overwrite_index = (index + QUEUE_LENGTH - 3) % QUEUE_LENGTH; // Third item index
            int overwrite_value = numbers[index];

            // Try to receive an item from the queue to make space
            if (xQueueReceive(xNumberQueue, NULL, 0) == pdPASS) {
                // Send the new item to the front of the queue
                if (xQueueSendToFront(xNumberQueue, &overwrite_value, 0) == pdPASS) {
                    printf("Overwritten at index %d with: %d\n", overwrite_index, overwrite_value);
                } else {
                    printf("Failed to overwrite queue\n");
                }
            } else {
                printf("Failed to receive item from queue\n");
            }
        }

        // Increment index (wraps around to start after reaching end of array)
        index = (index + 1) % QUEUE_LENGTH;

        // Wait for next period
        vTaskDelayUntil(&xLastWakeTime, pdMS_TO_TICKS(1000)); // 1 second delay
    }
}

// Task to receive and process numbers from the queue
void vReceiverTask(void *pvParameters) {
    TickType_t xLastWakeTime = xTaskGetTickCount();
    int received_number;

    for (;;) {
        // Receive number from queue
        if (xQueueReceive(xNumberQueue, &received_number, portMAX_DELAY) == pdPASS) {
            printf("Received from queue: %d\n", received_number);
        } else {
            printf("Failed to receive from queue\n");
        }

        // Wait for next period
        vTaskDelayUntil(&xLastWakeTime, pdMS_TO_TICKS(2000)); // 2 second delay
    }
}

int main(void) {
    // Create queue capable of holding 5 integers
    xNumberQueue = xQueueCreate(QUEUE_LENGTH, sizeof(int));

    if (xNumberQueue != NULL) {
        // Create sender task
        xTaskCreate(vSenderTask, "Sender", configMINIMAL_STACK_SIZE, NULL, 1, NULL);

        // Create receiver task
        xTaskCreate(vReceiverTask, "Receiver", configMINIMAL_STACK_SIZE, NULL, 2, NULL);

        // Start FreeRTOS scheduler
        vTaskStartScheduler();
    } else {
        printf("Failed to create queue\n");
    }

    // Main function should never reach here
    for (;;);
}

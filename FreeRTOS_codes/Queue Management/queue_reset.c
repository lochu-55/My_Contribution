#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include "semphr.h"
#include <stdio.h>
#include <stdarg.h>

// Mutex for synchronized printing
SemaphoreHandle_t xPrintMutex;

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

QueueHandle_t xQueue;

void vApplicationIdleHook(void)
{
}

void vSenderTask(void *pvParameters) {
    int ivalueToSend = 0;
    UBaseType_t uxNumberOfItems;

    for (;;) {
        // Check the number of items in the queue
        uxNumberOfItems = uxQueueMessagesWaiting(xQueue);

        if (uxNumberOfItems == 3) {
            // Reset the queue when it is full with 3 items
            xQueueReset(xQueue);
            xSemaphoreTake(xPrintMutex, portMAX_DELAY);
            vPrintString("Queue reset\n");
            xSemaphoreGive(xPrintMutex);
        } else {
            // Attempt to send items to the queue
            if (xQueueSend(xQueue, &ivalueToSend, portMAX_DELAY) == pdPASS) {
                xSemaphoreTake(xPrintMutex, portMAX_DELAY);
                vPrintString("Sent: %d\n", ivalueToSend);
                xSemaphoreGive(xPrintMutex);

                ivalueToSend++;
            } else {
                vPrintString("Failed to send: %d\n", ivalueToSend);
           
            }

            uxNumberOfItems = uxQueueMessagesWaiting(xQueue);

            xSemaphoreTake(xPrintMutex, portMAX_DELAY);
            vPrintString("Number of items in the queue: %d\n", uxNumberOfItems);
            xSemaphoreGive(xPrintMutex);
        }

        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

void vReceiverTask(void *pvParameters) {
    int receivedValue;

    for (;;) {
        // Attempt to receive items from the queue
        if (xQueueReceive(xQueue, &receivedValue, portMAX_DELAY) == pdPASS) {
            xSemaphoreTake(xPrintMutex, portMAX_DELAY);
            vPrintString("Received: %d\n", receivedValue);
            xSemaphoreGive(xPrintMutex);
        } else {

            vPrintString("Failed to receive\n");

        }

        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

int main(void) {
    xQueue = xQueueCreate(5, sizeof(int));
    xPrintMutex = xSemaphoreCreateMutex();

    if (xQueue != NULL && xPrintMutex != NULL) {
        xTaskCreate(vSenderTask, "Sender", 130, NULL, 1, NULL);
        xTaskCreate(vReceiverTask, "Receiver", configMINIMAL_STACK_SIZE, NULL, 1, NULL);
        vTaskStartScheduler();
    } else {
        vPrintString("Queue or Mutex creation failed\n");
    }

    for (;;) {
    }

}

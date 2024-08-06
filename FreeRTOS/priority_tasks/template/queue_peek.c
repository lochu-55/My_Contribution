#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include "semphr.h"
#include <stdio.h>
#include <stdarg.h>

SemaphoreHandle_t xPrintMutex;

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

void vApplicationIdleHook(void) { }

QueueHandle_t xQueue;

void vSenderTask(void *pvvar) {
    int ivalueToSend = 0;
    
    for (;;) {
           
            if (xQueueSendToBack(xQueue, &ivalueToSend, pdMS_TO_TICKS(100)) == pdPASS) {
                xSemaphoreTake(xPrintMutex, portMAX_DELAY);
                vPrintString("Sent: %d\n", ivalueToSend);
                xSemaphoreGive(xPrintMutex);
            } else {
               
                vPrintString("Queue is full. Failed to send: %d\n", ivalueToSend);
              
            }
             ivalueToSend ++ ;
            UBaseType_t uxNumberOfItems = uxQueueMessagesWaiting(xQueue);
            xSemaphoreTake(xPrintMutex, portMAX_DELAY);
            vPrintString("Number of items in the queue: %d\n", uxNumberOfItems);
            xSemaphoreGive(xPrintMutex);

            vTaskDelay(pdMS_TO_TICKS(200));
        }
    }


void vReceiverTask(void *pvvar) {
    int iReceivedValue;
    
    for (;;) {
        if (xQueueReceive(xQueue, &iReceivedValue, pdMS_TO_TICKS(100)) == pdPASS) {
            xSemaphoreTake(xPrintMutex, portMAX_DELAY);
            vPrintString("Received: %d\n", iReceivedValue);
            xSemaphoreGive(xPrintMutex);
        }

        vTaskDelay(pdMS_TO_TICKS(700));
    }
}

void vPeekTask(void *pvar) {
    int i;
    
    for (;;) {
        if (xQueue != NULL) {
            if (xQueuePeek(xQueue, &i, pdMS_TO_TICKS(100)) == pdPASS) {
                xSemaphoreTake(xPrintMutex, portMAX_DELAY);
                vPrintString("Peek value: %d\n", i);
                xSemaphoreGive(xPrintMutex);
            }
        } else {
         
            vPrintString("The queue could not be created\n");
       
        }

        vTaskDelay(pdMS_TO_TICKS(400)); // Add a delay to allow peeking periodically
    }
}

int main(void) {
    xQueue = xQueueCreate(5, sizeof(int));
    xPrintMutex = xSemaphoreCreateMutex();

    if (xQueue != NULL && xPrintMutex != NULL) {
        xTaskCreate(vSenderTask, "Sender", 130, NULL, 1, NULL);
        xTaskCreate(vReceiverTask, "Receiver", 130, NULL, 1, NULL);
        xTaskCreate(vPeekTask, "Peek", 130, NULL, 1, NULL);
        vTaskStartScheduler();
    } else {
        printf("Queue or Mutex creation failed\n");
    }

    for (;;) { }

}

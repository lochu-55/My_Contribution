#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>
#include <stdarg.h>

TaskHandle_t xHandlerTask = NULL;

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

void vApplicationIdleHook(void)
{
}


static void vPeriodicTask(void *pvParameters) {
    const TickType_t xDelay = pdMS_TO_TICKS(1000UL);

    for (;;) {
        vPrintString("Periodic task - About to notify the handler task.\r\n");

        // Increment the notification value
        xTaskNotify(xHandlerTask, 0, eIncrement);
        vTaskDelay(xDelay);

        // Set specific bits (bit 0 and bit 1)
        xTaskNotify(xHandlerTask, 1 | 2, eSetBits);
        vTaskDelay(xDelay);

        // Set the notification value to a new value (10)
        xTaskNotify(xHandlerTask, 10, eSetValueWithOverwrite);
        vTaskDelay(xDelay);

        // Set the notification value to a new value only if not updated (5)
        xTaskNotify(xHandlerTask, 5, eSetValueWithoutOverwrite);
        vTaskDelay(xDelay);

        vPrintString("Periodic task - Notifications sent.\r\n");
    }
}


static void vHandlerTask(void *pvParameters) {
    uint32_t ulNotificationValue;
    BaseType_t xResult;
    const TickType_t xMaxBlockTime = pdMS_TO_TICKS(2000);

    for (;;) {
        // Wait for a notification value to be received
        xResult = xTaskNotifyWait(0x00, 0xFFFFFFFF, &ulNotificationValue, xMaxBlockTime);

        if (xResult == pdPASS) {
            vPrintString("Handler task - Notification received with value: %u\r\n", ulNotificationValue);

            // Check if the notification was an increment
            if (ulNotificationValue == 1) {
                vPrintString("Handler task - Increment notification received.\r\n");
            }

            // Check specific bits
            if (ulNotificationValue == 3)
            {
                vPrintString("Handler task - Bit 0 is set.\r\n");
                vPrintString("Handler task - Bit 1 is set.\r\n");
            }

            // Check if notification value was set with overwrite
            if (ulNotificationValue == 10) {
                vPrintString("Handler task - Notification value set with overwrite: %u\r\n", ulNotificationValue);
            }

            // Check if notification value was set without overwrite
            if (ulNotificationValue == 5) {
                vPrintString("Handler task - Notification value set without overwrite: %u\r\n", ulNotificationValue);
            }

            // Process the notification value
            vPrintString("Handler task - Processing notification value: %u\r\n", ulNotificationValue);
        } else {
            vPrintString("Handler task - No notification received within the block time.\r\n");
        }
    }
}


int main(void) {
    xTaskCreate(vHandlerTask, "Handler", configMINIMAL_STACK_SIZE, NULL, 3, &xHandlerTask);
    xTaskCreate(vPeriodicTask, "Periodic", configMINIMAL_STACK_SIZE, NULL, 1, NULL);
    vTaskStartScheduler();
    
    for (;;) {
    }
}

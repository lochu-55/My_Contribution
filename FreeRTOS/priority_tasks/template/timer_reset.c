#include "FreeRTOS.h"
#include "task.h"
#include "timers.h"
#include <stdio.h>
#include <stdarg.h>

/* Define constants for timer period and reset intervals */
#define TIMER_PERIOD_MS 1000

/* Timer handle */
TimerHandle_t xTimer;

/* Task handle */
TaskHandle_t xResetTaskHandle = NULL;
void vApplicationIdleHook(void) {}

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

/* Timer callback function */
static void TimerCallback(TimerHandle_t xTimer) {
    TickType_t xTimeNow = xTaskGetTickCount();
    vPrintString("Timer callback executing at %d ticks\n", xTimeNow);
}

/* Task to reset the timer periodically */
static void vResetTimerTask(void *pvParameters) {
    int resetCount = 0;

    while (resetCount < 3) {
        // Simulated delay before each reset (less than timer period to ensure reset before expiry)
        vTaskDelay(pdMS_TO_TICKS(TIMER_PERIOD_MS / 2));

        // Reset the timer
        if (xTimerReset(xTimer, 0) != pdPASS) {
            // Timer reset failed
            vPrintString("Timer reset failed\n");
        } else {
            TickType_t xTimeNow = xTaskGetTickCount();
            vPrintString("Timer reset at %d ticks\n", xTimeNow);
            resetCount++;
        }
    }

    vPrintString("Timer reset task completed\n");

    // Suspend the reset task as its job is done
    vTaskSuspend(NULL);
}

int main(void) {
    // Create the timer with the initial period
    xTimer = xTimerCreate("MyTimer", pdMS_TO_TICKS(TIMER_PERIOD_MS), pdTRUE, NULL, TimerCallback);

    if (xTimer != NULL) {
        // Start the timer
        if (xTimerStart(xTimer, 0) != pdPASS) {
            // Timer start failed
            vPrintString("Timer start failed\n");
        }
    } else {
        // Timer creation failed
        vPrintString("Timer creation failed\n");
    }

    // Create the task to reset the timer
    if (xTaskCreate(vResetTimerTask, "ResetTimerTask", configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 1, &xResetTaskHandle) != pdPASS) {
        // Task creation failed
        vPrintString("Reset task creation failed\n");
        return 1;
    }

    // Start the scheduler
    vTaskStartScheduler();

    // The following code should not be reached
    for (;;) {}
 
}

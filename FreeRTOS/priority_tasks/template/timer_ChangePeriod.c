#include "FreeRTOS.h"
#include "task.h"
#include "timers.h"
#include <stdarg.h>
#include <stdio.h>

TickType_t xTimeNow;
int tickCounter = 0; // Counter to track the number of ticks

void vApplicationIdleHook(void) {}

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

/* Define constants for timer periods */
#define NORMAL_PERIOD_MS 2000
#define FAST_PERIOD_MS   500

/* Timer callback function */
static void TimerCallback(TimerHandle_t xTimer) {
    TickType_t xTimeNow;
    xTimeNow = xTaskGetTickCount();
    vPrintString("Timer callback executing at tick %d\n", xTimeNow);
    
    // Increment the tick counter
    tickCounter++;
    
    // Change the period after 5 ticks
    if (tickCounter == 5) {
        xTimerChangePeriod(xTimer, pdMS_TO_TICKS(FAST_PERIOD_MS), 0);

    }
}

int main(void) {
    // Create the timer with the initial normal period
    TimerHandle_t xTimer = xTimerCreate("MyTimer", pdMS_TO_TICKS(NORMAL_PERIOD_MS), pdTRUE, NULL, TimerCallback);

    if (xTimer != NULL) {
        // Start the timer
        if (xTimerStart(xTimer, 0) != pdPASS) {
            // Timer start failed
            printf("Timer start failed\n");
        }
    } else {
        // Timer creation failed
        printf("Timer creation failed\n");
    }

    // The FreeRTOS scheduler should never return
    vTaskStartScheduler();

    // The following code should not be reached
    for (;;) {}
}

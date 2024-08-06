#include "FreeRTOS.h"
#include "task.h"
#include "timers.h"
#include <stdarg.h>
#include <stdio.h>

void vApplicationIdleHook(void)
{
}

TickType_t xTimeNow;
uint32_t ulExecutionCount;

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

/* Define callback functions */
static void prvOneShotTimerCallback(TimerHandle_t xTimer);
static void prvAutoReloadTimerCallback(TimerHandle_t xTimer);

/* Define timer periods */
#define mainONE_SHOT_TIMER_PERIOD pdMS_TO_TICKS(3333) /* 3.333 seconds */
#define mainAUTO_RELOAD_TIMER_PERIOD pdMS_TO_TICKS(500) /* Half a second */


int main(void) {
    TimerHandle_t xAutoReloadTimer, xOneShotTimer;
    BaseType_t xTimer1Started, xTimer2Started;

    /* Create one-shot timer */
    xOneShotTimer = xTimerCreate("OneShot", mainONE_SHOT_TIMER_PERIOD, pdFALSE, 0, prvOneShotTimerCallback);

    /* Create auto-reload timer */
    xAutoReloadTimer = xTimerCreate("AutoReload", mainAUTO_RELOAD_TIMER_PERIOD, pdTRUE, 0, prvAutoReloadTimerCallback);
    
    // Check if timers were created successfully

    if (xOneShotTimer != NULL && xAutoReloadTimer != NULL) {
        /* Start the software timers */
        xTimer1Started = xTimerStart(xOneShotTimer, 0);
        xTimer2Started = xTimerStart(xAutoReloadTimer, 0);

        // Check if timers were started successfully

        if (xTimer1Started == pdPASS && xTimer2Started == pdPASS) {
            /* Start the scheduler */
            vTaskStartScheduler();
        }
    }

    /* As always, this line should not be reached */
    for (;;) {
        // Do nothing
    }
}


static void prvOneShotTimerCallback(TimerHandle_t xTimer) {

    // Obtain the current tick count.
    xTimeNow = xTaskGetTickCount();

    // Output a string to show the time at which the callback was executed.
    vPrintString("One-shot timer callback executing %lu\n", xTimeNow);
}

static void prvAutoReloadTimerCallback(TimerHandle_t xTimer) {

    // A count of the number of times this software timer has expired is stored in the timer's ID.
    // Obtain the ID, increment it, then save it as the new ID value.
    ulExecutionCount = (uint32_t)pvTimerGetTimerID(xTimer);
    ulExecutionCount++;
    vTimerSetTimerID(xTimer, (void *)ulExecutionCount);

    // Obtain the current tick count.
    xTimeNow = xTaskGetTickCount();

    // Output a string to show the time at which the callback was executed.
    vPrintString("Auto-reload timer callback executing %lu\n", xTimeNow);
    
    // Stop the auto-reload timer after it has executed 5 times.
    // This callback function executes in the context of the RTOS daemon task so must not call
    // any functions that might place the daemon task into the Blocked state.
    if (ulExecutionCount == 5) {
        xTimerStop(xTimer, 0);
    }
}

#include "FreeRTOS.h"
#include "task.h"
#include "timers.h"
#include <stdarg.h>
#include <stdio.h>

void vApplicationIdleHook(void)
{
}

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

    /* Check if timers were created successfully */
    if ((xOneShotTimer != NULL) && (xAutoReloadTimer != NULL)) {
        /* Start the timers */
        xTimer1Started = xTimerStart(xOneShotTimer, 0);
        xTimer2Started = xTimerStart(xAutoReloadTimer, 0);

        /* Start the scheduler if timers started successfully */
        if ((xTimer1Started == pdPASS) && (xTimer2Started == pdPASS)) {
            vTaskStartScheduler(); /* This call will never return */
        }
    }

    /* This line should not be reached */
    for (;;) {
        /* Do nothing */
    }
}

/* One-shot timer callback function */
static void prvOneShotTimerCallback(TimerHandle_t xTimer) {
    TickType_t xTimeNow;
    xTimeNow = xTaskGetTickCount();
    vPrintString("One-shot timer callback executing %d\n", xTimeNow);
}

/* Auto-reload timer callback function */
static void prvAutoReloadTimerCallback(TimerHandle_t xTimer) {
    TickType_t xTimeNow;
    xTimeNow = xTaskGetTickCount();
    vPrintString("Auto-reload timer callback executing%d\n", xTimeNow);
}

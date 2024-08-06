#include "FreeRTOS.h"
#include "task.h"
#include "timers.h"
#include "event_groups.h"
#include <stdio.h>
#include <stdarg.h>

/* Definitions for the event bits in the event group. */
#define mainFIRST_TASK_BIT ( 1UL << 0UL ) /* Event bit 0, which is set by a task. */
#define mainSECOND_TASK_BIT ( 1UL << 1UL ) /* Event bit 1, which is set by a task. */
#define mainISR_BIT ( 1UL << 2UL ) /* Event bit 2, which is set by an ISR. */

EventGroupHandle_t xEventGroup;

void vPrintString(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    fflush(stdout);
}

void vApplicationIdleHook(void) { }
/* Function to print messages from the RTOS daemon task */
void vPrintStringFromDaemonTask(void *pvParameter, uint32_t ulValue) {
    const char *pcString = (const char *)pvParameter;
    printf("%s\n", pcString);
}

/* Task that sets event bits in the event group */
static void vEventBitSettingTask(void *pvParameters) {
    const TickType_t xDelay200ms = pdMS_TO_TICKS(200UL);

    for (;;) {
        /* Delay for a short while before starting the next loop. */
        vTaskDelay(xDelay200ms);

        /* Print out a message to say event bit 0 is about to be set by the task, then set event bit 0. */
        vPrintString("Bit setting task -\t about to set bit 0.\r\n");
        xEventGroupSetBits(xEventGroup, mainFIRST_TASK_BIT);

        /* Delay for a short while before setting the other bit. */
        vTaskDelay(xDelay200ms);

        /* Print out a message to say event bit 1 is about to be set by the task, then set event bit 1. */
        vPrintString("Bit setting task -\t about to set bit 1.\r\n");
        xEventGroupSetBits(xEventGroup, mainSECOND_TASK_BIT);
    }
}

/* ISR that sets an event bit */
static uint32_t ulEventBitSettingISR(void) {
    /* The string is not printed within the interrupt service routine, but is instead
    sent to the RTOS daemon task for printing. It is therefore declared static to ensure 
    the compiler does not allocate the string on the stack of the ISR, as the ISR's stack 
    frame will not exist when the string is printed from the daemon task. */
    static const char *pcString = "Bit setting ISR -\t about to set bit 2.\r\n";
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    /* Print out a message to say bit 2 is about to be set. Messages cannot be
    printed from an ISR, so defer the actual output to the RTOS daemon task by
    pending a function call to run in the context of the RTOS daemon task. */
    xTimerPendFunctionCallFromISR(vPrintStringFromDaemonTask, (void *)pcString, 0, &xHigherPriorityTaskWoken);

    /* Set bit 2 in the event group. */
    xEventGroupSetBitsFromISR(xEventGroup, mainISR_BIT, &xHigherPriorityTaskWoken);

    /* If xHigherPriorityTaskWoken equals pdTRUE, then calling portYIELD_FROM_ISR() will request a context switch. */
    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);

    return 0; /* In case the return type is needed */
}

/* Task that reads event bits from the event group */
static void vEventBitReadingTask(void *pvParameters) {
    EventBits_t xEventGroupValue;
    const EventBits_t xBitsToWaitFor = (mainFIRST_TASK_BIT | mainSECOND_TASK_BIT | mainISR_BIT);

    for (;;) {
        /* Block to wait for event bits to become set within the event group. */
        xEventGroupValue = xEventGroupWaitBits(
            xEventGroup,         /* The event group to read. */
            xBitsToWaitFor,      /* Bits to test. */
            pdTRUE,              /* Clear bits on exit if the unblock condition is met. */
            pdFALSE,             /* Don't wait for all bits. */
            portMAX_DELAY);      /* Don't time out. */

        /* Print a message for each bit that was set. */
        if ((xEventGroupValue & mainFIRST_TASK_BIT) != 0) {
            vPrintString("Bit reading task -\t Event bit 0 was set\r\n");
        }
        if ((xEventGroupValue & mainSECOND_TASK_BIT) != 0) {
            vPrintString("Bit reading task -\t Event bit 1 was set\r\n");
        }
        if ((xEventGroupValue & mainISR_BIT) != 0) {
            vPrintString("Bit reading task -\t Event bit 2 was set\r\n");
        }
    }
}

/* Function to simulate a software interrupt */
static void vInterruptGenerator(void *pvParameters) {
    const TickType_t xDelay500ms = pdMS_TO_TICKS(500UL);

    for (;;) {
        vTaskDelay(xDelay500ms);
        /* Simulate an interrupt by calling the ISR handler function directly */
        ulEventBitSettingISR();
    }
}

int main(void) {
    /* Before an event group can be used it must first be created. */
    xEventGroup = xEventGroupCreate();

    if (xEventGroup != NULL) {
        /* Create the task that sets event bits in the event group. */
        xTaskCreate(vEventBitSettingTask, "Bit Setter", 1000, NULL, 1, NULL);

        /* Create the task that waits for event bits to get set in the event group. */
        xTaskCreate(vEventBitReadingTask, "Bit Reader", 1000, NULL, 2, NULL);

        /* Create the task that is used to periodically generate a software interrupt. */
        xTaskCreate(vInterruptGenerator, "Int Gen", 1000, NULL, 3, NULL);

        /* Start the scheduler so the created tasks start executing. */
        vTaskStartScheduler();
    }

    /* The following line should never be reached. */
    for (;;) {}

}


//BaseType_t xTaskNotifyGive( TaskHandle_t xTaskToNotify );

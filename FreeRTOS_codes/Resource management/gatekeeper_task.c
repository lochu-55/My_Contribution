#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include <stdio.h>
#include <stdlib.h>

// Define the maximum number of messages the queue can hold
#define QUEUE_LENGTH 5
void vApplicationIdleHook(void) {
    // Idle hook implementation (optional)
}

// Queue handle for passing messages to the gatekeeper task
QueueHandle_t xPrintQueue;

// Array of strings that tasks and interrupt will print via the gatekeeper
static char *pcStringsToPrint[] = {
    "Task 1 ****************************************************\r\n",
    "Task 2 ----------------------------------------------------\r\n",
    "Message printed from the tick hook interrupt ##############\r\n"
};

// Task to manage access to standard output
static void prvStdioGatekeeperTask(void *pvParameters) {
    char *pcMessageToPrint;
    
    for (;;) {
        // Wait for a message to arrive in the queue
        xQueueReceive(xPrintQueue, &pcMessageToPrint, portMAX_DELAY);
        
        // Output the received string
        printf("%s", pcMessageToPrint);

        fflush(stdout); // Ensure output is flushed
        
        // Loop back to wait for the next message
    }
}

// Task to send messages to the gatekeeper task
static void prvPrintTask(void *pvParameters) {
    int iIndexToString;
    const TickType_t xMaxBlockTimeTicks = 0x20;
    
    // Extract the index to the string from the task parameter
    iIndexToString = (int)pvParameters;
    
    for (;;) {
        // Send a pointer to the string to the gatekeeper task via the queue
        xQueueSendToBack(xPrintQueue, &(pcStringsToPrint[iIndexToString]), 0);
        
        // Wait a pseudo random time
        vTaskDelay((rand() % xMaxBlockTimeTicks));
    }
}

// Interrupt handler to send a message to the gatekeeper task
void vApplicationTickHook(void) {
    static int iCount = 0;
    
    // Print a message every 200 ticks
    iCount++;
    if (iCount >= 200) {
        // Send a pointer to the message via the queue
        xQueueSendToFrontFromISR(xPrintQueue, &(pcStringsToPrint[2]), NULL);
        
        // Reset the count to print the message again in 200 ticks
        iCount = 0;
    }
}

// Main function
int main(void) {
    // Create the queue to pass messages to the gatekeeper task
    xPrintQueue = xQueueCreate(QUEUE_LENGTH, sizeof(char *));
    
    // Check if the queue was created successfully
    if (xPrintQueue != NULL) {
        // Create tasks that send messages to the gatekeeper task
        xTaskCreate(prvPrintTask, "Print1", 100, (void *)0, 1, NULL);
        xTaskCreate(prvPrintTask, "Print2", 100, (void *)1, 2, NULL);
        
        // Create the gatekeeper task that manages access to stdout
        xTaskCreate(prvStdioGatekeeperTask, "Gatekeeper", 100, NULL, 0, NULL);
        
        // Start the FreeRTOS scheduler
        vTaskStartScheduler();
    }
    
    // If the scheduler starts successfully, main() will not reach here
    for (;;);
    
}

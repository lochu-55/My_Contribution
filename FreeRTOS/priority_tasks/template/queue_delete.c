#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include "stdio.h"

// Define the queue handle
QueueHandle_t xQueue;
TaskHandle_t sender_task;
TaskHandle_t receiver_task;

void vApplicationIdleHook(void)
{
}

// Sender Task
void vSenderTask(void *pvParameters)
{
    int32_t lValueToSend;
    BaseType_t xStatus;

    // Send three elements to the queue
    for (lValueToSend = 0; lValueToSend < 3; lValueToSend++)
    {
        xStatus = xQueueSendToBack(xQueue, &lValueToSend, 0);
        printf("Sender: Sending %d to the queue.\n", lValueToSend);

        if (xStatus != pdPASS)
        {
            printf("Sender: Failed to send %d to the queue.\n", lValueToSend);
        }
    }

    // Indicate that the sender task has completed sending
    //printf("Sender: Completed sending all elements. Deleting sender task.\n");

    // Delete the sender task
    vTaskDelete(sender_task);
}

// Receiver Task
void vReceiverTask(void *pvParameters)
{
    int32_t lReceivedValue;
    BaseType_t xStatus;
    const TickType_t xTicksToWait = pdMS_TO_TICKS(100);

    // Receive three elements from the queue
    for (int i = 0; i < 3; i++)
    {
        
        xStatus = xQueueReceive(xQueue, &lReceivedValue, xTicksToWait);
        if (xStatus == pdPASS)
        {
            printf("Receiver: Received value %d from the queue.\n", lReceivedValue);
        }
        else
        {
            printf("Receiver: Failed to receive value %d from the queue.\n", i);
        }
    }

    // Delete the queue
    vQueueDelete(xQueue);
    printf("Receiver: All elements received. Deleting the queue.\n");

    // Indicate that the receiver task is completed
    //printf("Receiver: Deleting receiver task.\n");

    // Delete the receiver task
    vTaskDelete(receiver_task);
}

int main(void)
{
    // Create the queue
    xQueue = xQueueCreate(3, sizeof(int32_t));

    if (xQueue != NULL)
    {
        // Indicate queue creation success
        printf("Main: Queue created successfully.\n");

        // Create the sender task
        xTaskCreate(vSenderTask, "Sender", configMINIMAL_STACK_SIZE, NULL, 1, &sender_task);

        // Create the receiver task
        xTaskCreate(vReceiverTask, "Receiver", configMINIMAL_STACK_SIZE, NULL, 2, &receiver_task);

        // Start the scheduler
        printf("Main: Starting the scheduler.\n");
        vTaskStartScheduler();
    }
    else
    {
        // Queue could not be created
        printf("Main: Queue could not be created.\n");
    }

    // If all is well, the scheduler will now be running, and the following line will never be reached.
    for (;;);

}

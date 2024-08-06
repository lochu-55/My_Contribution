#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>

/* Use this fuunction to implement delays. The parameter passed is in milliseconds. */
extern void delay(uint32_t t);

void vApplicationIdleHook(void)
{
}

TaskHandle_t t1 = NULL;
TaskHandle_t t2 = NULL;

void task1 (void *p){
    
    while(1){
        printf("%s",p);
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

void task2 (void *p){

    while(1){
        printf("%s",p);
        vTaskDelay(pdMS_TO_TICKS(1000));
        
    }
}


void task3(void* pvParameters) {
    while(1){
        // Get the number of tasks
        UBaseType_t taskCount = uxTaskGetNumberOfTasks();
        printf("Number of tasks: %lu\n", (unsigned long)taskCount);

        // Iterate through tasks and print their details
        for (UBaseType_t i = 0; i < taskCount; i++) {
            TaskStatus_t taskStatusArray[taskCount];
            UBaseType_t taskCountActual = uxTaskGetSystemState(taskStatusArray, taskCount, NULL);

            for (UBaseType_t j = 0; j < taskCountActual; j++) {
                TaskStatus_t *taskStatus = &taskStatusArray[j];
                printf("Task Name: %s\n", taskStatus->pcTaskName);
                printf("Task Handle: %p\n", (void*)taskStatus->xHandle);
                printf("Task State: %lu\n", (unsigned long)taskStatus->eCurrentState);
                printf("Task Priority: %lu\n", taskStatus->uxCurrentPriority);
                printf("Task Stack High Water Mark: %lu\n", (unsigned long)taskStatus->usStackHighWaterMark);
            }
        }

        vTaskDelay(pdMS_TO_TICKS(5000));  // Print every 5 seconds
    }
}
int main(void)
{
    char* s1 = "lochu\n";
    char* s2 = "vara\n";
	xTaskCreate(task1,"task1",100,s1,0,&t1);
    xTaskCreate(task2,"task2",100,s2,1,&t2);
    xTaskCreate(task3, "task3",100,NULL, 2, NULL); 
    /* Write your code here*/
    vTaskStartScheduler();
    printf("Starting project\n");
	while (1)
	{
		
	}
}

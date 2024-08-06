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





/*
Number of tasks: 5
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 89
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 119
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 89
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 89
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 89
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 119
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 89
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 119
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 89
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 89
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 89
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 119
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 89
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 119
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 89
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
vara
lochu
vara
lochu
vara
lochu
vara
lochu
vara
lochu
Number of tasks: 5
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 37
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 117
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 28
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 37
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 28
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 117
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 37
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 117
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 28
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 37
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 28
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 117
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
Task Name: task3
Task Handle: 20000620
Task State: 0
Task Priority: 2
Task Stack High Water Mark: 34
Task Name: task2
Task Handle: 20000428
Task State: 1
Task Priority: 1
Task Stack High Water Mark: 37
Task Name: IDLE
Task Handle: 20000890
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 117
Task Name: task1
Task Handle: 20000230
Task State: 1
Task Priority: 0
Task Stack High Water Mark: 28
Task Name: Tmr Svc
Task Handle: 20000da0
Task State: 2
Task Priority: 2
Task Stack High Water Mark: 233
vara
lochu
vara
lochu
vara
lochu
vara
lochu
vara
lochu
*/

#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>

void vApplicationIdleHook(void)
{
}

TaskHandle_t mytaskHandle = NULL;
TaskHandle_t task_suspend = NULL;

void mytask1 (void *p) {
    int count =0;
    while(1){
        printf("hello,world : %d\n",count++);
        vTaskDelay(1000);
    }
}


void mytask2 (void *p) {
    while(1) {
        printf("task suspended..!\n");
        vTaskSuspend(mytaskHandle);
        vTaskDelay(5000);
        printf("task resumed..!\n");
        vTaskResume(mytaskHandle);
        vTaskDelay(5000);

    }
}

int main(void)
{
    printf("Starting project\n");
    xTaskCreate(mytask1,"task1",100,NULL,tskIDLE_PRIORITY,&mytaskHandle);
    xTaskCreate(mytask2,"task2",100,NULL,tskIDLE_PRIORITY,&task_suspend);
    vTaskStartScheduler();
    /* Write your code here*/
	while (1)
	{
		
	}
}

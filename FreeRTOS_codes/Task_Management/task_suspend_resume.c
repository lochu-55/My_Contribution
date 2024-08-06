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
        vTaskDelay(5000);
        vTaskSuspend(mytaskHandle);
        printf("task suspended..!\n");
        vTaskDelay(5000);
        vTaskResume(mytaskHandle);
        printf("task resumed..!\n");
    }
}

int main(void)
{
    xTaskCreate(mytask1,"task1",100,NULL,tskIDLE_PRIORITY,&mytaskHandle);
    xTaskCreate(mytask2,"task2",100,NULL,tskIDLE_PRIORITY,&task_suspend);
    vTaskStartScheduler();
    /* Write your code here*/
    printf("Starting project\n");
	while (1)
	{
		
	}
}

/*
hello,world : 0
hello,world : 1
hello,world : 2
hello,world : 3
hello,world : 4
task suspended..!
hello,world : 5
task resumed..!
hello,world : 6
hello,world : 7
hello,world : 8
hello,world : 9
task suspended..!
hello,world : 10
task resumed..!
hello,world : 11
hello,world : 12
hello,world : 13
hello,world : 14
task suspended..!
hello,world : 15
task resumed..!
hello,world : 16
hello,world : 17
hello,world : 18
hello,world : 19
task suspended..!
hello,world : 20
task resumed..!
hello,world : 21
hello,world : 22
hello,world : 23
hello,world : 24
task suspended..!

*/

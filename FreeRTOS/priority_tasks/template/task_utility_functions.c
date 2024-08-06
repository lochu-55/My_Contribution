#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>

void vApplicationIdleHook(void)
{
}

TaskHandle_t mytaskHandle1 = NULL;
TaskHandle_t mytaskHandle2 = NULL;
char mytaskList[500];

void mytask1 (void *p) {
    int count =0;
    while(1){
        printf("hello,world : %d\n",count++);
        vTaskDelay(1000);
        printf("current task running name : %s\n",pcTaskGetName(mytaskHandle1));
        if (count == 3){
            vTaskDelete(xTaskGetHandle("task1"));
        }
    }
}


void mytask2 (void *p) {
    int i = 0;
    while(1) {
        printf("hey Testies...%d!\n",i);
        i++;
        printf("current task running name : %s\n",pcTaskGetName(mytaskHandle2));
        vTaskDelay(1000);
        
        TaskHandle_t TaskName = xTaskGetCurrentTaskHandle();
        if (i==5) {
           vTaskDelete(TaskName); 
        }
    }
}


void tasklist (void *p) {
    while(1) {
        vTaskList(mytaskList);
        printf("%s\r\n",mytaskList);
        printf("the total tick : %d\n",xTaskGetTickCount());
        vTaskDelay(2000);
    }
}

int main(void)
{
    xTaskCreate(mytask1,"task1",100,NULL,2,&mytaskHandle1);
    xTaskCreate(mytask2,"task2",100,NULL,1,&mytaskHandle2);
    xTaskCreate(tasklist,"task3",100,NULL,tskIDLE_PRIORITY,NULL);
    vTaskStartScheduler();
    /* Write your code here*/
    printf("Starting project\n");
	while (1)
	{
		
	}
}

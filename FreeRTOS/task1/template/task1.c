#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>

void vApplicationIdleHook(void)
{
}

TaskHandle_t mytaskHandle = NULL;

void mytask1 (void *p) {
    int count =0;
    while(1){
        printf("hello,world : %d\n",count++);
        vTaskDelay(1000);
    }
}
int main(void)
{
    xTaskCreate(mytask1,"task1",100,NULL,tskIDLE_PRIORITY,&mytaskHandle);
    vTaskStartScheduler();
    /* Write your code here*/
    printf("Starting project\n");
	while (1)
	{
		
	}
}

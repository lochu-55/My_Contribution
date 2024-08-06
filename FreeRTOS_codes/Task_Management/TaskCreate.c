#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>

/* Use this fuunction to implement delays. The parameter passed is in milliseconds. */
extern void delay(uint32_t t);

void vApplicationIdleHook(void)
{
}

TaskHandle_t mytaskHandle = NULL;

void mytask1 (void *p) {
    int count =0;
    while(1){
        printf("hello,world : %d",count++);
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


/*
hello,world : 0
hello,world : 1
hello,world : 2
hello,world : 3
hello,world : 4
hello,world : 5
*/
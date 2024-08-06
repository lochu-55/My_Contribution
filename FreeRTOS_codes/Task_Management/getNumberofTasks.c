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
        BaseType_t TaskCount = uxTaskGetNumberOfTasks(); 
        printf("%s",p);
        printf("Number of tasks : %d\n",(int)TaskCount);
        vTaskDelay(pdMS_TO_TICKS(1000));
        
    }
}
int main(void)
{
    char* s1 = "lochu\n";
    char* s2 = "vara\n";
	xTaskCreate(task1,"task1",100,s1,1,&t1);
    xTaskCreate(task2,"task2",100,s2,2,&t2);
    /* Write your code here*/
    vTaskStartScheduler();
    printf("Starting project\n");
	while (1)
	{
		
	}
}



/*
vara
Number of tasks : 4
lochu
vara
Number of tasks : 4
lochu
vara
Number of tasks : 4
lochu
vara
Number of tasks : 4
lochu
*/

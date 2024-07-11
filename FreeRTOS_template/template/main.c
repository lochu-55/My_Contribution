#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>

/* Use this fuunction to implement delays. The parameter passed is in milliseconds. */
extern void delay(uint32_t t);

void vApplicationIdleHook(void)
{
}

int main(void)
{
	SystemCoreClockUpdate();
	
	SysTick_Config(SystemCoreClock/1000);
	NVIC_SetPriority(SysTick_IRQn, 1);
    /* Write your code here*/
    printf("Starting project\n");
	while (1)
	{
		
	}
}

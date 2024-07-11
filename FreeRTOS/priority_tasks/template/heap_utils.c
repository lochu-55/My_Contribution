#include "heap_utils.h"
#include "FreeRTOS.h"

// Define a global variable to store the total heap size
static size_t totalHeapSize = configTOTAL_HEAP_SIZE;

size_t xPortGetHeapSize(void) {
    // Return the total heap size
    return totalHeapSize;
}

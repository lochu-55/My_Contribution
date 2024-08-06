import micropython

# Display memory info
micropython.mem_info()

"""
Output:
stack: 476 out of 15360
GC: total: 61248, used: 1504, free: 59744
 No. of 1-blocks: 15, 2-blocks: 6, max blk sz: 40, max free sz: 3722



The output you're seeing from micropython.mem_info() provides information about memory usage and garbage collection (GC) statistics in a MicroPython environment. Let's break down each section of the output:

Memory Information Breakdown:
Stack Usage:

stack: 476 out of 15360: This indicates the stack usage of your program.
476 is the amount of stack space currently in use.
15360 is the total stack space available.
This shows how much of the stack is currently allocated and used by your program.
Garbage Collection (GC) Statistics:

GC: total: 61248, used: 1504, free: 59744:
total: Total heap memory available for allocation.
used: Amount of heap memory currently in use.
free: Remaining free heap memory available for allocation.
These values collectively describe the current heap memory usage in your MicroPython environment.
Block Information:

No. of 1-blocks: 15, 2-blocks: 6:
Indicates the number of blocks of memory currently allocated in the heap.
1-blocks are single blocks of memory.
2-blocks are blocks of memory that are larger and span multiple blocks.
max blk sz: 40, max free sz: 3722:
max blk sz: Maximum size of a single block of memory allocated.
max free sz: Maximum size of a contiguous free block of memory available."""
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "cacheutils.h"

/*
 * VMs typically virtualize some 'dangerous' instructions such as RDTSC, 
 * which measures the number of cycles since the processor is reset. 
 *
 * Not having high precision timing information prevents most cache side-channel
 * timing attacks, but we can create covert channels by timing not just an
 * individual cache access, but a sequence of accesses. If e.g., N=1000 accesses
 * are hits, the aggregate time should be low. If N=1000 accesses are misses, it
 * should be high. It is the job of the transmitter to make sure that all N
 * accesses are all hits or all misses.
 */
#ifndef N
#define N 4  /* Accesses Per Experiment */
#endif

/*
 * Number of separate experiments to run. 
 * Each experiment runs N accesses. 
 */
#ifndef MEASUREMENTS
#define MEASUREMENTS 1024*16
#endif

/*
 * Size of the array being accessed
 */
#ifndef ARRAY_SIZE
#define ARRAY_SIZE 1
#endif

/*
 * Histogram bin count
 */
#ifndef BINS 
#define BINS 50
#endif

size_t array[ARRAY_SIZE];
size_t hit_histogram[BINS];
size_t miss_histogram[BINS];

/*
 * Time N accesses, most of which should hit
 */
size_t repeat_hit(void* addr) {
    size_t time = rdtsc();
    for (int i=0; i<N; i++)
        maccess(addr);
    size_t delta = rdtsc() - time;
    
    // these values can get very large, so cut them down in for the histogram
    delta = delta / 10;

    return delta;
}

/*
 * Time N accesses, most of which should miss because we perform a flush
 * after every access
 */
size_t repeat_miss(void* addr)
{
    size_t time = rdtsc();
    for (int i=0; i<N; i++) {
        maccess(addr);
        flush(addr);
    }
    size_t delta = rdtsc() - time;

    // these values can get very large, so cut them down in for the histogram
    delta = delta / 10;

    return delta;
}

/*
 * This program measures the time to perform N hits and the time for N 
 * misses. By setting a time threhold that clearely separates misses from hits, 
 * we can use repeated cache accesses as a covert channel. The goal of this
 * program is to learn what threashold works on your machine.
 */
int main(int argc, char** argv)
{
    memset(array, -1, ARRAY_SIZE*sizeof(size_t));

    for (int i = 0; i < MEASUREMENTS; ++i) {
        size_t d = repeat_hit(array+ARRAY_SIZE/2);
        hit_histogram[MIN(BINS-1, d)]++;
    }

    for (int i = 0; i < MEASUREMENTS; ++i) {
        size_t d = repeat_miss(array + ARRAY_SIZE/2);
        miss_histogram[MIN(BINS-1, d)]++;
    }

    for (size_t i = 0; i < BINS; ++i) {
        printf("%3zu: %10zu %10zu\n", i, hit_histogram[i], miss_histogram[i]);
    }
}

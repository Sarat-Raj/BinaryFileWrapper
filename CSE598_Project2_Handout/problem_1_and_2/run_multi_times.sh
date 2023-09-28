#!/bin/bash

# Output file to store the results
output_file="iteration_bandwidth_results.txt"

# Clear existing data in the output file
# echo -n "" > "$output_file"

# array_sizes=()

# for((i=8192;i<=16777216;i*=2));do
#     array_sizes+=("$i")
# done

# # Loop to test different array sizes
# for array_size in "${array_sizes[@]}"
# do
# Compile the STREAM benchmark with the current array size
gcc -DSTREAM_ARRAY_SIZE=$1 -fopenmp -O3 simple_stream.c -o simple_stream -mcmodel=large

# Run the benchmark
export OMP_NUM_THREADS=1  # Use a single thread
./simple_stream >> "$output_file"
# done
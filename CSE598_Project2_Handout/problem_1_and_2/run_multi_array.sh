#!/bin/bash

# Output file to store the results
output_file="memory_bandwidth_results.txt"

# Clear existing data in the output file
echo -n "" > "$output_file"

array_sizes=()

for((i=8192;i<=16777216;i*=2));do
    array_sizes+=("$i")
done

# Loop to test different array sizes
for array_size in "${array_sizes[@]}"
do
    # Compile the STREAM benchmark with the current array size
    gcc -DSTREAM_ARRAY_SIZE=$array_size -fopenmp -O3 simple_stream.c -o simple_stream -mcmodel=large

    # Run the benchmark
    export OMP_NUM_THREADS=1  # Use a single thread
    ./simple_stream >> $output_file
done

# Generate the scatter plot using Gnuplot
# gnuplot <<EOF
# set terminal pngcairo size 800,600
# set output 'memory_bandwidth_scatter.png'
# set title 'Memory Bandwidth vs. Array Size'
# set xlabel 'Array Size (elements)'
# set ylabel 'Memory Bandwidth (MiB/s)'
# set logscale x
# plot "$output_file" using 1:2 with points title 'Bandwidth'
# EOF
# 
# echo "Scatter plot saved as memory_bandwidth_scatter.png"

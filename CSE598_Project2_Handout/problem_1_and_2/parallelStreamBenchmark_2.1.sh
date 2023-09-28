#!/bin/bash

output_file="Output_parallel2_1.txt"
echo -n "" > "$output_file"

gcc -DSTREAM_ARRAY_SIZE=131072 -fopenmp -O3 simple_stream.c -o simple_stream -mcmodel=large
command2="./simple_stream >> "$output_file""
num_times_to_rum="$1"
if [ $# -eq 0 ]; then
    echo "Usage: $0 <number of times to run>"
    echo "Since nothing is given, running 5 times parallelly"
    num_times_to_rum=5
fi



# Run commands in the background

for((i=1;i<=num_times_to_rum;i++));do
    eval "$command2" &
done

# Wait for all background processes to finish
wait

# echo "All commands are done"

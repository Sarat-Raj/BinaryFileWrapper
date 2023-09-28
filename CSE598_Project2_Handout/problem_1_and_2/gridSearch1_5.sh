#!/bin/bash                                                                                                                                                                                                

# Set the output file                                                                                                                                                                                      
output_file="grid_search_results.txt"
echo -n "" > "$output_file"

# Number of times to run the benchmark for each pair of NTIMES and Arraysize                                                                                                                               
num_runs=15

#export OMP_NUM_THREADS=3                                                                                                                                                                                  

# Loop through NTIMES values                                                                                                                                                                               
for NTIMES in 1 2 4 8 16; do
    # Loop through array sizes from 10K to 100M in multiples of 10                                                                                                                                         
    for((array_size=8192;array_size<=16777216;array_size*=2)); do
        # Initialize arrays to store benchmark results                                                                                                                                                     
        bandwidths=()

        # Compile simplestream.c with the current array size and NTIMES value                                                                                                                              
        gcc -DSTREAM_ARRAY_SIZE=$array_size -DNTIMES=$NTIMES -fopenmp -O3 simple_stream.c -o simple_stream

        # Run the benchmark multiple times and store the output                                                                                                                                            
        for ((i = 1; i <= num_runs; i++)); do
            benchmark_output=$(./simple_stream)

            # Extract the "Best Rate" value using awk                                                                                                                                                      
            best_rate=$(echo "$benchmark_output" | grep "Copy:" | awk '{print $2}')

            # Append the benchmark result to the array                                                                                                                                                     
            bandwidths+=("$best_rate")
        done

        # Calculate the average and standard deviation                                                                                                                                                     
        average_bandwidth=$(printf "%s\n" "${bandwidths[@]}" | awk '{s+=$1} END {print s/NR}')
        std_deviation_bandwidth=$(printf "%s\n" "${bandwidths[@]}" | awk -v mean="$average_bandwidth" '{sumsq+=($1-mean)^2} END {print sqrt(sumsq/NR)}')

        # Append the NTIMES, array size, average bandwidth, and standard deviation to the output file                                                                                                      
        echo "NTIMES=$NTIMES, ARRAY_SIZE=$array_size, Avg_Bandwidth=$average_bandwidth, Std_Dev_Bandwidth=$std_deviation_bandwidth" >> "$output_file"
    done
done
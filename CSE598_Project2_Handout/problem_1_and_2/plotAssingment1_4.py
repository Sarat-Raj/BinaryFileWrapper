import numpy as np
import subprocess
import matplotlib.pyplot as plt
import re
import os

def iterfunc(array_size):
    # Define the command to run the Bash script with arguments
    bash_script = "./run_multi_times.sh"
    for x in range(10):
    # Build the command as a list
        command = [bash_script, str(array_size)]
        # Run the command and wait for it to complete
        process = subprocess.Popen(command)
        process.wait()
        # Check the return code to determine if the script executed successfully
        if process.returncode == 0:
            pass
            #print("Bash script executed successfully.",x)
        else: pass
            #print("Bash script execution failed.",x)
        


def extraction_func():
    # Initialize lists to store the extracted values
    array_size = []
    #threads = []
    # clocks = []
    rates = []
    # avgs = []
    # min_times = []
    # max_times = []

    # Define regular expressions for the patterns
    pattern_array_size = r'\$\$array_size\$pythonreference\$\$\s*(\d+)'
    #pattern_thread = r'\$\$thread\$pythonreference\$\$\s*(\d+)'
    #pattern_clock = r'\$\$clocktick\$pythonreference\$\$\s*(\d+)'
    pattern_rate = r'\$\$rate\$pythonreference\$\$\s*([\d.]+)'
    #pattern_avg = r'\$\$avg\$pythonreference\$\$\s*([\d.]+)'
    #pattern_min = r'\$\$min\$pythonreference\$\$\s*([\d.]+)'
    #pattern_max = r'\$\$max\$pythonreference\$\$\s*([\d.]+)'

    # Read the file 'recordThreadoutput.txt'
    with open('iteration_bandwidth_results.txt', 'r') as file:
        input_text = file.read()

    # Split the input text into sections based on ----End of Execution----
    sections = input_text.split('----End of Execution----')

    # Iterate through sections and process each one
    for section in sections:
        # Search for the patterns in the current section
        array_size_match = re.search(pattern_array_size, section)
        #clock_match = re.search(pattern_clock, section)
        rate_match = re.search(pattern_rate, section)
        # avg_match = re.search(pattern_avg, section)
        # min_match = re.search(pattern_min, section)
        # max_match = re.search(pattern_max, section)
        # Extract values if the patterns were found in the current section
        if array_size_match:
            array_size.append(int(array_size_match.group(1)))
        # if clock_match:
        #     clocks.append(int(clock_match.group(1)))
        if rate_match:
            rates.append(float(rate_match.group(1)))
        # if avg_match:
        #     avgs.append(float(avg_match.group(1)))
        # if min_match:
        #     min_times.append(float(min_match.group(1)))
        # if max_match:
        #    max_times.append(float(max_match.group(1)))

    #rates=[0,0,0,0,0,0,0,0,0,0,0,0]+rates[:-4]
    # Print the extracted values from all sections
    #print("array_size:", array_size)
    # print("Clocks:", clocks)
    #print("Rates:", rates)
    # print("Avgs:", avgs)
    # print("Min Times:", min_times)
    # print("Max Times:", max_times)
    os.remove("iteration_bandwidth_results.txt")
    return array_size, rates

def standarad_dev_func(multi_result_rates):
    std_deviation_multi_result_rates = "{:.1f}".format(np.std(multi_result_rates))
    return std_deviation_multi_result_rates

def plot(multi_result_array_size,multi_result_rates):

    # Create the graph
    plt.figure(figsize=(10, 6),dpi=300)
    x=len(multi_result_rates)
    # print("multi_result_rates length :",x)
    # print("multi_result_rates",multi_result_rates)
    plt.scatter(range(x), multi_result_rates, marker='o', linestyle='-')
    plt.xlabel('Size of Array : '+str(multi_result_array_size))
    plt.ylabel('Memory Bandwidth (MiB/s)')
    plt.title('Memory Bandwidth vs. Size of Array')
    plt.grid(True)
    #plt.yticks(rates)

    # Show the graph or save it as an image file
    plt.savefig("Problem"+str(multi_result_array_size)+".jpg")


if __name__=="__main__":
    array_sizes = [8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]
    multi_result_array_size=[]
    multi_result_rates=[]
    for array_size in array_sizes:
        iterfunc(array_size)

        result_array_size,result_rates = extraction_func()
        plot(array_size,result_rates)
        multi_result_array_size.append(result_array_size[0])
        print("multi_result_array_size",multi_result_array_size)

        print("multi_result_rates ",result_rates)

        

        multi_result_rates.append(standarad_dev_func(result_rates))

        print("multi_result_rates after sd",multi_result_rates)

        print("\n\n\n")
        
    
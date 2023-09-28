import numpy as np
import subprocess
import matplotlib.pyplot as plt
import re
import os
import time
        


def extraction_func():
    # Initialize lists to store the extracted values
    array_size = []
    rates = []

    # Define regular expressions for the patterns
    pattern_array_size = r'\$\$array_size\$pythonreference\$\$\s*(\d+)'
    pattern_rate = r'\$\$rate\$pythonreference\$\$\s*([\d.]+)'

    # Read the file 'recordThreadoutput.txt'
    with open('Output_parallel2_1.txt', 'r') as file:
        input_text = file.read()

    # Split the input text into sections based on ----End of Execution----
    sections = input_text.split('----End of Execution----')

    # Iterate through sections and process each one
    for section in sections:
        # Search for the patterns in the current section
        array_size_match = re.search(pattern_array_size, section)
        rate_match = re.search(pattern_rate, section)

        # Extract values if the patterns were found in the current section
        if array_size_match:
            array_size.append(int(array_size_match.group(1)))
        if rate_match:
            rates.append(float(rate_match.group(1)))

    # print("array_size:", array_size)
    # print("Rates:", rates)
    return array_size, rates


def plot(parallel, multi_result_rates):

    # Create the graph
    plt.figure(figsize=(10, 6),dpi=300)
    plt.bar(range(parallel), multi_result_rates)
    plt.xlabel('Size of parallel : '+str(parallel))
    plt.ylabel('Memory Bandwidth (MiB/s)')
    plt.title('Memory Bandwidth vs. Size of Array')
    plt.grid(True)
    #plt.yticks(rates)

    # Show the graph or save it as an image file
    plt.savefig("Problem 2_1 num of parallel "+str(parallel)+".jpg")
    plt.close()

def plot1(parallel,multi_result_SD_rates):

    # Create the graph
    plt.figure(figsize=(10, 6),dpi=300)
    plt.bar(parallel, multi_result_SD_rates)
    plt.xlabel('Size of parallel : '+str(parallel))
    plt.ylabel('AVG rates')
    plt.title('Size of Array vs sd rates')
    plt.grid(True)
    #plt.yticks(rates)

    # Show the graph or save it as an image file
    plt.savefig("AVG rates vs parallel.jpg")


if __name__=="__main__":
    
    multi_result_rates=[]
    result_AVG_rates=[]
    for par in [1,2,3,4,5,6,7,8,9,10]:
        command = f"./parallelStreamBenchmark_2.1.sh {par}"
        os.system(command)
        time.sleep(5)
        result_array_size,result_rates = extraction_func()
        print("result_rates",result_rates)
        plot(par,result_rates)        
        print("Number of parallel processess: ", par)
        result_AVG_rates="{:.1f}".format(sum(result_rates)/len(result_rates))
        multi_result_rates.append(result_AVG_rates)
    print("multi_result_AVG_rates: ",multi_result_rates)
    print("\n\n\n")
    plot1([1,2,3,4,5,6,7,8,9,10], multi_result_rates)
    
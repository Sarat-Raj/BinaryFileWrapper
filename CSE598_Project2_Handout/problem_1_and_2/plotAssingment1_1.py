import matplotlib.pyplot as plt
import re

# Initialize lists to store the extracted values
threads = []
clocks = []
rates = []
avgs = []
min_times = []
max_times = []

# Define regular expressions for the patterns
pattern_thread = r'\$\$thread\$pythonreference\$\$\s*(\d+)'
pattern_clock = r'\$\$clocktick\$pythonreference\$\$\s*(\d+)'
pattern_rate = r'\$\$rate\$pythonreference\$\$\s*([\d.]+)'
pattern_avg = r'\$\$avg\$pythonreference\$\$\s*([\d.]+)'
pattern_min = r'\$\$min\$pythonreference\$\$\s*([\d.]+)'
pattern_max = r'\$\$max\$pythonreference\$\$\s*([\d.]+)'

# Read the file 'recordThreadoutput.txt'
with open('recordThreadoutput.txt', 'r') as file:
    input_text = file.read()

# Split the input text into sections based on ----End of Execution----
sections = input_text.split('----End of Execution----')

# Iterate through sections and process each one
for section in sections:
    # Search for the patterns in the current section
    thread_match = re.search(pattern_thread, section)
    clock_match = re.search(pattern_clock, section)
    rate_match = re.search(pattern_rate, section)
    avg_match = re.search(pattern_avg, section)
    min_match = re.search(pattern_min, section)
    max_match = re.search(pattern_max, section)

    # Extract values if the patterns were found in the current section
    if thread_match:
        threads.append(int(thread_match.group(1)))
    if clock_match:
        clocks.append(int(clock_match.group(1)))
    if rate_match:
        rates.append(float(rate_match.group(1)))
    if avg_match:
        avgs.append(float(avg_match.group(1)))
    if min_match:
        min_times.append(float(min_match.group(1)))
    if max_match:
        max_times.append(float(max_match.group(1)))

# Print the extracted values from all sections
print("Threads:", threads)
print("Clocks:", clocks)
print("Rates:", rates)
print("Avgs:", avgs)
print("Min Times:", min_times)
print("Max Times:", max_times)



# Create the graph
plt.figure(figsize=(8, 6))
plt.plot(threads, avgs, marker='o', linestyle='-')
plt.xlabel('Number of Threads')
plt.ylabel('Memory Bandwidth (MiB/s)')
plt.title('Memory Bandwidth vs. Number of Threads')
plt.grid(True)

# Show the graph or save it as an image file
plt.savefig("Problem1_1.jpg")

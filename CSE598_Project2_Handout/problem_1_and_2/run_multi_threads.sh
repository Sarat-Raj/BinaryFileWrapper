
# Clear existing data in the output file
echo -n "" > recordThreadoutput.txt

for threads in {1..40}; do
    export OMP_NUM_THREADS=$threads
    ./simple_stream >> recordThreadoutput.txt
done

for threads in {1..16}; do
    export OMP_NUM_THREADS=$threads
    ./simple_stream >> recordThreadoutput.txt
done

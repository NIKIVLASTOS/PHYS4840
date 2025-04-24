#!/bin/bash

# As this is on a mac it took me and Dr. Miller a while but we found out I have to use gdate instead of just date 
# when timing so you might have to change this if you're running it to test it.

# Also, I have to run the command in my terminal ">$ brew install coreutils" to get the gdate to work if you have something
# Other than a Mac you could probably just remove the g in gdate and run it and it should work

echo "Compiling oddball.f90..."

start_compile=$(gdate +%s.%N)
gfortran oddball.f90 -o oddball.exe
end_compile=$(gdate +%s.%N)

compile_time=$(echo "$end_compile - $start_compile" | bc -l)

echo "Running oddball.exe..."

start_exec=$(gdate +%s.%N)
./oddball.exe
end_exec=$(gdate +%s.%N)

exec_time=$(echo "$end_exec - $start_exec" | bc -l)

echo "Compilation time: $compile_time seconds"
echo "Execution time: $exec_time seconds"

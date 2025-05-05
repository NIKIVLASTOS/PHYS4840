#=========================
# Makefile for Schrödinger Solver
#=========================

FC = gfortran
FFLAGS = -O2 -Wall -fopenmp
EXEC = schrodinger_solver
SRC = main_solver.f90 matrix_tools.f90

all: $(EXEC)

$(EXEC): $(SRC)
	$(FC) $(FFLAGS) -c matrix_tools.f90
	$(FC) $(FFLAGS) -o $(EXEC) main_solver.f90 matrix_tools.o

run: $(EXEC)
	./$(EXEC)
	python3 plot_results.py

clean:
	rm -f $(EXEC) *.o *.mod *.txt *.png
	rm -rf plots

.PHONY: all run clean

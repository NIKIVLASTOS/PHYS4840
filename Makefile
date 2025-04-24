#=========================
# File: Makefile
#=========================
FC = gfortran
FFLAGS = -O2 -Wall -fopenmp

SRC = src/main_solver.f90 src/matrix_tools.f90
EXEC = schrodinger_solver

all: $(EXEC)

$(EXEC): $(SRC)
	$(FC) $(FFLAGS) -o $(EXEC) $(SRC)

run: $(EXEC)
	./$(EXEC)
	python3 plot/plot_results.py

clean:
	rm -f $(EXEC)
	rm -f output/*.txt
	rm -f plots/*.png

.PHONY: all run clean

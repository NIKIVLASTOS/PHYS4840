#==========================                                          
# Fixed Makefile                                                     
#==========================

FC = gfortran                                                        # Fortran compiler
FFLAGS = -O2 -Wall                                                   # Compiler flags: optimize, show all warnings

MODS = potential_functions.f90 matrix_tools.f90 normalization.f90   # Module source files
MAIN = main_solver.f90                                              # Main program file
EXEC = schrodinger_solver                                           # Executable name

all: $(EXEC)                                                        # Default target: build the executable

$(EXEC): $(MODS) $(MAIN)                                            # Rule to compile and link all source files
	$(FC) $(FFLAGS) -c $(MODS)                                       # Compile modules to object files
	$(FC) $(FFLAGS) -o $(EXEC) *.o $(MAIN)                           # Link object files with main to create executable

run: $(EXEC)                                                        # Rule to run the program
	./$(EXEC)                                                       # Execute Fortran program
	python3 plot_results.py                                         # Run Python script to plot results

clean:                                                              # Rule to clean up build artifacts
	rm -f $(EXEC) *.o *.mod                                         # Remove executable, object files, and module files
	rm -rf __pycache__ plots                                       # Remove Python cache and plots folder

!=======================
! File: main_solver.f90 (Updated to read input file)
!=======================
program SchrodingerSolver
  use matrix_tools
  implicit none

  ! Input parameters
  real(8) :: xmin, xmax, dx, param
  integer :: Nx, neigs, potential_type
  
  ! Grid and problem variables
  real(8), allocatable :: x(:), V(:), H(:,:), psi(:,:), eigvals(:)
  integer :: i

  ! === Read input file ===
  open(unit=9, file="test/test_case_ho.inp", status="old")
  read(9,*) xmin
  read(9,*) xmax
  read(9,*) Nx
  read(9,*) neigs
  read(9,*) potential_type
  read(9,*) param
  close(9)

  allocate(x(Nx), V(Nx), H(Nx,Nx), psi(Nx, neigs), eigvals(neigs))

  ! Define grid
  dx = (xmax - xmin) / (Nx - 1)
  do i = 1, Nx
    x(i) = xmin + (i - 1) * dx
  end do

  ! === Define potential based on input ===
  select case (potential_type)
    case (1)  ! Harmonic oscillator: V(x) = kx^2
      do i = 1, Nx
        V(i) = param * x(i)**2
      end do
    case default
      print *, "ERROR: Unknown potential type."
      stop
  end select

  ! Build Hamiltonian
  call build_hamiltonian(H, V, dx, Nx)

  ! Solve eigenvalue problem
  call jacobi_solver(H, eigvals, psi, Nx, neigs)

  ! Normalize eigenfunctions
  call normalize_wavefunctions(psi, x, Nx, neigs)

  ! Output results
  open(unit=10, file="output/xgrid.txt", status="replace")
  write(10, *) (x(i), i=1,Nx)
  close(10)

  open(unit=11, file="output/eigenvalues.txt", status="replace")
  write(11, *) (eigvals(i), i=1,neigs)
  close(11)

  open(unit=12, file="output/wavefunctions.txt", status="replace")
  do i = 1, neigs
    write(12, *) (psi(j, i), j=1, Nx)
  end do
  close(12)

  print *, "Computation complete. Output files written."
end program SchrodingerSolver




! OUTPUTS
! xgrid.txt              ← Space grid (Nx values)
! eigenvalues.txt        ← First neigs energy eigenvalues
! wavefunctions.txt      ← Each row is ψₙ(x) for n = 1 to neigs

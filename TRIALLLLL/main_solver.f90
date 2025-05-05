program SchrodingerSolver
  use matrix_tools
  implicit none

  ! Input parameters
  real(8) :: xmin, xmax, dx, param
  integer :: Nx, neigs, potential_type
  real(8), allocatable :: x(:), V(:), H(:,:), psi(:,:), eigvals(:)
  integer :: i, j

  ! === Read input file ===
  open(unit=9, file="test_case_ho.inp", status="old")
  read(9,*) xmin
  read(9,*) xmax
  read(9,*) Nx
  read(9,*) neigs
  read(9,*) potential_type
  read(9,*) param
  close(9)

  allocate(x(Nx), V(Nx), H(Nx,Nx), psi(Nx, neigs), eigvals(neigs))

  dx = (xmax - xmin) / (Nx - 1)
  do i = 1, Nx
    x(i) = xmin + (i - 1) * dx
  end do

  ! === Define potential ===
  select case (potential_type)
    case (1)  ! Harmonic oscillator: V(x) = kx^2
      V = param * x**2

    case (2)  ! Infinite square well: V = 0 inside, high outside
      do i = 1, Nx
        if (x(i) > xmin .and. x(i) < xmax) then
          V(i) = 0.0d0
        else
          V(i) = 1.0d10
        end if
      end do

    case default
      print *, "ERROR: Unknown potential type."
      stop
  end select

  call build_hamiltonian(H, V, dx, Nx)
  call jacobi_solver(H, eigvals, psi, Nx, neigs)
  call normalize_wavefunctions(psi, x, Nx, neigs)

  open(10, file="xgrid.txt", status="replace")
  write(10, *) (x(i), i=1,Nx)
  close(10)

  open(11, file="eigenvalues.txt", status="replace")
  write(11, *) (eigvals(i), i=1,neigs)
  close(11)

  open(12, file="wavefunctions.txt", status="replace")
  do i = 1, neigs
    write(12, *) (psi(j,i), j=1,Nx)
  end do
  close(12)

  print *, "Computation complete. Output files written."
end program SchrodingerSolver


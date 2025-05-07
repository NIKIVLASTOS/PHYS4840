!==============================                                             
! File: main_solver.f90                                                     ! Main program for solving the 1D Schrödinger equation
!==============================

program main_solver                                                          ! Start
  use potential_functions                                                    ! Use module for potential energy functions (from potential_functions.f90)
  use matrix_tools                                                           ! Use module for Jacobi diagonalization (from matrix_tools.f90)
  use normalization                                                          ! Use module for wavefunction normalization (from normalization.f90)
  implicit none                                                             ! Require all variables to be explicitly declared (Nothing is implicit)
  integer :: Nx, nstates, i, pot_type                                        ! Grid points, number of states, loop index, potential type
  real(8) :: xmin, xmax, dx, V0, width                                       ! Domain bounds, grid spacing, well depth, domain width
  real(8), allocatable :: x(:), V(:), H(:,:), eigvals(:), eigvecs(:,:)      ! Arrays: grid, potential, Hamiltonian, eigenvalues/vectors
  character(len=100) :: infile                                               ! Input file name
  character(len=200) :: line                                                 ! Buffer for reading lines
  integer :: count, ios                                                      ! Line count and I/O status

  infile = 'input.txt'                                                       ! input file name (Can change to whatever you would like (dr. Joyce or whover grading))
  count = 0                                                                  ! Initialize line counter

  ! === Read input file, skip comments and blank lines ===
  open(unit=10, file=infile, status='old')                                   ! Open input file
  do while (.true.)                                                          ! Loop over lines
    read(10, '(A)', iostat=ios) line                                         ! Read line
    if (ios /= 0) exit                                                       ! Exit loop at end of file or error
    line = trim(adjustl(line))                                               ! Remove whitespace
    if (line /= "" .and. line(1:1) /= "!") then                               ! Skip comments and blanks (assuming ! is how comments in input file are written (e.g. Fortran))
      count = count + 1                                                      ! Increment line counter
      print *, "Reading line ", count, ": ", trim(line)                      ! Print line for debugging
      select case (count)                                                   ! Determine which line it is reading
      case (1)
        read(line, *, iostat=ios) xmin, xmax, Nx                             ! Read grid bounds and number of points
        if (ios /= 0) then
          print *, "Failed to parse line 1 as xmin xmax Nx"                 ! Error message
          stop                                                               ! Exit if input fails
        end if
      case (2)
        read(line, *, iostat=ios) pot_type                                   ! Read potential type
      case (3)
        read(line, *, iostat=ios) nstates                                    ! Read number of eigenstates
      case (4)
        read(line, *, iostat=ios) V0                                         ! Read V0 (used for finite well)
      end select
    end if
  end do
  close(10)                                                                  ! Close input file

  allocate(x(Nx), V(Nx), H(Nx,Nx), eigvals(Nx), eigvecs(Nx,Nx))              ! Allocate arrays for grid, potential, Hamiltonian, results

  width = xmax - xmin                                                        ! Compute domain width
  dx = width / real(Nx - 1, kind=8)                                          ! Compute grid spacing

  ! === Construct symmetric spatial grid and potential ===
  do i = 1, Nx
    x(i) = -0.5d0 * width + real(i - 1, kind=8) * dx                         ! Centered grid: x from  negative width/2 to  positive width/2
    select case (pot_type)
    case (1)
      V(i) = 100.0d0 * harmonic_oscillator(x(i))                            ! Scale factor added harmonic oscillator potential
    case (2)
      V(i) = infinite_square_well(x(i), -0.5d0 * width + dx, 0.5d0 * width - dx) ! Infinite square well
    case (3)
      V(i) = finite_square_well(x(i), -0.5d0 * width, 0.5d0 * width, V0)     ! Finite well across domain
    case (4)
      V(i) = step_potential(x(i))                                             ! Normal step function
    case (5)
      V(i) = stepped_trap(x(i))                                                ! Use custom step + wall potential
    case (6)
      V(i) = step_barrier(x(i))
    end select
  end do

  print *, "dx = ", dx                                                       ! Output/print grid spacing
  print *, "x(Nx/2 + 1) = ", x(Nx/2 + 1)                                     ! Output/print center point
  print *, "Potential type:", pot_type                                       ! Output/print potential type
  print *, "Sample V(x):", V(1), V(Nx/2), V(Nx)                              ! Output/print sample values of potential

  ! === Build Hamiltonian ===
  H = 0.0d0                                                                  ! Initialize Hamiltonian to zero
  do i = 1, Nx
    H(i,i) = 1.0d0/dx**2 + V(i)                                              ! Main diagonal: kinetic + potential
    if (i > 1)     H(i,i-1) = -0.5d0/dx**2                                   ! Lower diagonal: -h(bar)²/2m del² term
    if (i < Nx)    H(i,i+1) = -0.5d0/dx**2                                   ! Upper diagonal
  end do

  ! === Save Hamiltonian I PUT THIS IN FOR DEBBUGING ===
  open(88, file='H_sample.txt')                                              ! Write small sample of H to file
  do i = 1, min(Nx, 10)
    write(88, '(10f10.5)') H(i,1:min(Nx,10))                                  ! Write a small matrix block
  end do
  close(88)

  call jacobi(H, Nx, eigvals, eigvecs, 1000000, 1.0d-10)                        ! Diagonalize Hamiltonian
  call sort_eigenpairs(eigvals, eigvecs, Nx)                                 ! Sort eigenpairs in ascending order
  call normalize_wavefunctions(eigvecs, dx)                                  ! Normalize wavefunctions

  ! === Save results ===
  open(22, file='xgrid.txt')                                                 ! Save spatial grid (to xgrid.txt)
  do i = 1, Nx
    write(22,*) x(i)
  end do
  close(22)

  open(33, file='eigenvalues.txt')                                           ! Save eigenvalues (to eigenvalues.txt)
  do i = 1, nstates
    write(33,*) eigvals(i)
  end do
  close(33)

  open(44, file='wavefunctions.txt')                                         ! Save eigenvectors (wavefunctions) (to wavefunctions.txt)
  do i = 1, nstates
    write(44,'(10000f20.12)') eigvecs(:,i)
  end do
  close(44)

  print *, "Computation complete. Output files written."                     ! print message to user (or Dr.Joyce/grader)

contains                                                                      ! Begin internal procedure block

  subroutine sort_eigenpairs(eigvals, eigvecs, n)                            ! Subroutine to sort eigenvalues/vectors
    implicit none
    integer, intent(in) :: n
    real(8), intent(inout) :: eigvals(n)                                     ! Eigenvalues to be sorted
    real(8), intent(inout) :: eigvecs(n,n)                                   ! Corresponding eigenvectors
    integer :: i, j, k
    real(8) :: temp_val
    real(8), allocatable :: temp_vec(:)

    allocate(temp_vec(n))                                                    ! Temporary vector for swapping
    do i = 1, n - 1
      k = i
      do j = i + 1, n
        if (eigvals(j) < eigvals(k)) k = j                                   ! Find index of minimum eigenvalue
      end do
      if (k /= i) then                                                       ! Swap if needed
        temp_val = eigvals(i)
        eigvals(i) = eigvals(k)
        eigvals(k) = temp_val

        temp_vec = eigvecs(:,i)
        eigvecs(:,i) = eigvecs(:,k)
        eigvecs(:,k) = temp_vec
      end if
    end do
    deallocate(temp_vec)                                                     ! Clean up
  end subroutine sort_eigenpairs                                             ! End subroutine

end program main_solver                                                      ! End 




!========================
! File: matrix_tools.f90
!========================
module matrix_tools
  implicit none
contains

  !---------------------------------------------
  ! Build the Hamiltonian matrix H = T + V(x)
  !---------------------------------------------
subroutine build_hamiltonian(H, V, dx, N)
  real(8), intent(out) :: H(N, N)
  real(8), intent(in)  :: V(N), dx
  integer, intent(in)  :: N
  integer :: i

  ! Start with zero matrix
  H = 0.0d0

  ! Build finite difference Laplacian (tridiagonal)
  do i = 1, N
    H(i, i) = -2.0d0 / dx**2
    if (i > 1) H(i, i-1) = 1.0d0 / dx**2
    if (i < N) H(i, i+1) = 1.0d0 / dx**2
  end do

  ! Apply prefactor for kinetic energy operator: -ħ²/2m = -1/2 (in atomic units)
  H = -0.5d0 * H

  ! Add potential V(x) to diagonal
  do i = 1, N
    H(i, i) = H(i, i) + V(i)
  end do
end subroutine build_hamiltonian

  !---------------------------------------------------
  ! Jacobi method to find eigenvalues/eigenvectors
  !---------------------------------------------------
   subroutine jacobi_solver(A, eigvals, eigvecs, N, neigs)
    implicit none
    real(8), intent(in out) :: A(N,N)
    real(8), intent(out) :: eigvals(neigs), eigvecs(N, neigs)
    integer, intent(in) :: N, neigs
    real(8) :: V(N,N), tol, theta, t, c, s, tau, temp
    integer :: i, j, k, l, iter, max_iter
    real(8) :: max_val
    integer :: idx(N)  ! ✅ Declare at the top, before any executable code

    V = 0.0d0
    do i = 1, N
      V(i,i) = 1.0d0
    end do

    tol = 1.0d-10
    max_iter = 1000

    do iter = 1, max_iter
      ! Find largest off-diagonal element
      max_val = 0.0d0
      do i = 1, N-1
        do j = i+1, N
          if (abs(A(i,j)) > max_val) then
            max_val = abs(A(i,j))
            k = i
            l = j
          end if
        end do
      end do
      if (max_val < tol) exit

      ! Compute rotation parameters
      tau = (A(l,l) - A(k,k)) / (2.0d0 * A(k,l))
      t = sign(1.0d0, tau) / (abs(tau) + sqrt(1.0d0 + tau**2))
      c = 1.0d0 / sqrt(1.0d0 + t**2)
      s = t * c

      ! Perform rotation
      do i = 1, N
        if (i /= k .and. i /= l) then
          temp = A(i,k)
          A(i,k) = c*temp - s*A(i,l)
          A(k,i) = A(i,k)
          A(i,l) = s*temp + c*A(i,l)
          A(l,i) = A(i,l)
        end if
      end do

      temp = c*c*A(k,k) - 2.0d0*s*c*A(k,l) + s*s*A(l,l)
      A(l,l) = s*s*A(k,k) + 2.0d0*s*c*A(k,l) + c*c*A(l,l)
      A(k,k) = temp
      A(k,l) = 0.0d0
      A(l,k) = 0.0d0

      do i = 1, N
        temp = V(i,k)
        V(i,k) = c*temp - s*V(i,l)
        V(i,l) = s*temp + c*V(i,l)
      end do
    end do

    ! Extract eigenvalues and initialize index array
    do i = 1, N
      eigvals(i) = A(i,i)
      idx(i) = i
    end do

    call sort_indices(eigvals, idx, N)

    ! Store lowest neigs sorted eigenvalues/eigenvectors
    do i = 1, neigs
      eigvals(i) = A(idx(i), idx(i))
      eigvecs(:,i) = V(:,idx(i))
    end do
  end subroutine jacobi_solver


  !---------------------------------------------
  ! Normalize wavefunctions ψ(x)
  !---------------------------------------------
  subroutine normalize_wavefunctions(psi, x, Nx, neigs)
    real(8), intent(in out) :: psi(Nx, neigs)
    real(8), intent(in) :: x(Nx)
    integer, intent(in) :: Nx, neigs
    integer :: i, j
    real(8) :: norm, dx

    dx = x(2) - x(1)
    do j = 1, neigs
      norm = 0.0d0
      do i = 1, Nx
        norm = norm + psi(i, j)**2
      end do
      norm = sqrt(norm * dx)
      psi(:, j) = psi(:, j) / norm
    end do
  end subroutine normalize_wavefunctions

  !------------------------------------------------
  ! Utility: Sort indices of array in ascending order
  !------------------------------------------------
  subroutine sort_indices(arr, idx, N)
    real(8), intent(in) :: arr(N)
    integer, intent(in out) :: idx(N)
    integer, intent(in) :: N
    integer :: i, j, tmp
    do i = 1, N - 1
      do j = i + 1, N
        if (arr(idx(j)) < arr(idx(i))) then
          tmp = idx(i)
          idx(i) = idx(j)
          idx(j) = tmp
        end if
      end do
    end do
  end subroutine sort_indices

end module matrix_tools
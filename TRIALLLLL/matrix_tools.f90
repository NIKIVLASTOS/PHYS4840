module matrix_tools
  implicit none
contains

  !--------------------------------------------------
  ! Build the Hamiltonian matrix H = T + V(x)
  !--------------------------------------------------
  subroutine build_hamiltonian(H, V, dx, N)
    implicit none
    real(8), intent(out) :: H(N,N)
    real(8), intent(in)  :: V(N), dx
    integer, intent(in)  :: N
    integer :: i

    H = 0.0d0

    do i = 1, N
      ! Diagonal element includes potential
      H(i,i) = -2.0d0 / dx**2 + V(i)

      ! Off-diagonal elements (ensure symmetry)
      if (i > 1) then
        H(i,i-1) = 1.0d0 / dx**2
        H(i-1,i) = H(i,i-1)
      end if
    end do

    ! Apply kinetic energy prefactor (-ħ²/2m = -1/2 in a.u.)
    H = -0.5d0 * H
  end subroutine build_hamiltonian

  !--------------------------------------------------
  ! Jacobi eigenvalue solver for symmetric matrices
  !--------------------------------------------------
  subroutine jacobi_solver(A, eigvals, eigvecs, N, neigs)
    implicit none
    real(8), intent(inout) :: A(N,N)
    real(8), intent(out)   :: eigvals(neigs), eigvecs(N, neigs)
    integer, intent(in)    :: N, neigs

    real(8) :: V(N,N), tol, t, c, s, tau, temp
    real(8) :: max_val
    integer :: i, j, k, l, iter, max_iter
    integer :: idx(N)
    real(8) :: eigvals_unsorted(N)

    ! Initialize eigenvector matrix
    V = 0.0d0
    do i = 1, N
      V(i,i) = 1.0d0
    end do

    tol = 1.0d-12
    max_iter = 10000

    ! Jacobi rotation loop
    do iter = 1, max_iter
      max_val = 0.0d0
      k = 1; l = 2
      do i = 1, N-1
        do j = i+1, N
          if (abs(A(i,j)) > max_val) then
            max_val = abs(A(i,j))
            k = i; l = j
          end if
        end do
      end do
      if (max_val < tol) exit

      tau = (A(l,l) - A(k,k)) / (2.0d0 * A(k,l))
      t = sign(1.0d0, tau) / (abs(tau) + sqrt(1.0d0 + tau*tau))
      c = 1.0d0 / sqrt(1.0d0 + t*t)
      s = t * c

      ! Rotate matrix A
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

      ! Rotate eigenvectors
      do i = 1, N
        temp = V(i,k)
        V(i,k) = c*temp - s*V(i,l)
        V(i,l) = s*temp + c*V(i,l)
      end do
    end do

    ! === Extract and sort eigenvalues and vectors ===
    do i = 1, N
      eigvals_unsorted(i) = A(i,i)
      idx(i) = i
    end do

    call sort_indices(eigvals_unsorted, idx, N)

    do i = 1, neigs
      eigvals(i) = eigvals_unsorted(i)
      eigvecs(:,i) = V(:,idx(i))
    end do
  end subroutine jacobi_solver

  !--------------------------------------------------
  ! Normalize wavefunctions using rectangular rule
  !--------------------------------------------------
  subroutine normalize_wavefunctions(psi, x, Nx, neigs)
    real(8), intent(inout) :: psi(Nx, neigs)
    real(8), intent(in)    :: x(Nx)
    integer, intent(in)    :: Nx, neigs
    real(8) :: dx, norm
    integer :: i, j

    dx = x(2) - x(1)
    do j = 1, neigs
      norm = 0.0d0
      do i = 1, Nx
        norm = norm + psi(i,j)**2
      end do
      norm = sqrt(norm * dx)
      psi(:,j) = psi(:,j) / norm
    end do
  end subroutine normalize_wavefunctions

  !--------------------------------------------------
  ! Sort indices of array in ascending order
  !--------------------------------------------------
  subroutine sort_indices(arr, idx, N)
    real(8), intent(in)    :: arr(N)
    integer, intent(inout) :: idx(N)
    integer, intent(in)    :: N
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



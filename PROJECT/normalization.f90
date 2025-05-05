!==============================                                              
! File: normalization.f90                                                   
!==============================

module normalization                                                         ! Define module "normalization routines"
  implicit none                                                              ! Require all variables to be explicitly declared (Nothing is implicit)
contains                                                                     ! start

  subroutine normalize_wavefunctions(psi, dx)                               ! Subroutine to normalize each wavefunction psi(x)
    implicit none                                                            ! no implicit
    real(8), intent(in) :: dx                                                ! Input: grid spacing
    real(8), intent(inout) :: psi(:,:)                                       ! Input/output: matrix of wavefunctions (nstates * Nx)
    integer :: n                                                             ! Index for wavefunction
    real(8) :: norm                                                          ! Norm of each wavefunction

    do n = 1, size(psi, 1)                                                   ! Loop over each wavefunction
      norm = sqrt(sum(psi(n,:)**2) * dx)                                     ! Compute L2 norm using rectangle rule: integral of psi^2 dx approx equals sum * dx
      psi(n,:) = psi(n,:) / norm                                             ! Normalize: by doing psi / absolute of psi 
    end do                                                                   ! End loop
  end subroutine normalize_wavefunctions                                     ! End subroutine

end module normalization                                                     ! End module

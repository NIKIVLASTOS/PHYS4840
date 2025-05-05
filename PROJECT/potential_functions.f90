!==============================                                       
! File: potential_functions.f90                                      
!==============================                                       

module potential_functions                                            ! Define a module for 'potential energy functions'
  implicit none                                                       ! Require all variables to be explicitly declared (Nothing is implicit)
contains                                                              ! Begin module procedures

  function harmonic_oscillator(x) result(v)                           ! This is the Harmonic oscillator potential: V(x) = (1/2) * m * w² * x²
    implicit none                                                     ! No implicit 
    real(8), intent(in) :: x                                          ! Input: position x
    real(8) :: v                                                      ! Output: potential energy (I chose to denote with v) at x
    real(8), parameter :: m = 1.0d0, omega = 1.0d0                    ! Parameters: mass and angular frequency (natural units)
    v = 0.5d0 * m * omega**2 * x**2                                   ! Compute V(x) = 1/2 * m * w² * x²
  end function harmonic_oscillator                                    ! End function

  function infinite_square_well(x, xmin, xmax) result(v)              ! This is the infinite square well potential
    implicit none                                                     ! No implicit 
    real(8), intent(in) :: x, xmin, xmax                              ! Inputs: position and well boundaries
    real(8) :: v                                                      ! Output: potential energy at x
    if (x < xmin .or. x > xmax) then                                  ! Outside the well
      v = 1.0d12                                                      ! Assign a large number to approximate infinity (b/c can't do infinity in a computer)
    else                                                              ! This else is for inside the well
      v = 0.0d0                                                       ! Zero potential energy (we can arbitrarily set it to 0)
    end if                                                            ! End conditional (if/else)
  end function infinite_square_well                                   ! End function

  function finite_square_well(x, xmin, xmax, V0) result(v)            ! This Is the Finite square well potential
    implicit none                                                     ! No implicit 
    real(8), intent(in) :: x, xmin, xmax, V0                          ! Inputs: position, boundaries, and barrier height
    real(8) :: v                                                      ! Output: potential energy at x
    if (x < xmin .or. x > xmax) then                                  ! Outside the well
      v = V0                                                          ! Assign potential barrier height
    else                                                              ! This else is for inside the well
      v = 0.0d0                                                       ! Zero potential energy
    end if                                                            ! End conditional (if/else)
  end function finite_square_well                                     ! End function

end module potential_functions                                        ! End of whole module

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

  function infinite_square_well(x, xmin, xmax) result(v)
    implicit none
    real(8), intent(in) :: x, xmin, xmax
    real(8) :: v
    real(8), parameter :: V_INF = 1.0d20  ! Use a very large value to simulate infinite wall
    real(8) :: x1, x2

    ! Shift edges inward by 1 unit
    x1 = xmin + 1.0d0
    x2 = xmax - 1.0d0

    if (x <= x1 .or. x >= x2) then
      v = V_INF
    else
      v = 0.0d0
    end if
  end function infinite_square_well



  function finite_square_well(x, xmin, xmax, V0) result(v)
    implicit none
    real(8), intent(in) :: x, xmin, xmax, V0
    real(8) :: v
    real(8) :: wall_left, wall_right

    wall_left = xmin + 2.0d0
    wall_right = xmax - 2.0d0

    if (x < wall_left .or. x > wall_right) then
      v = V0     ! Outside the well
    else
      v = 0.0d0  ! Inside the well
    end if
  end function finite_square_well

  function step_potential(x) result(v)
    implicit none
    real(8), intent(in) :: x
    real(8) :: v
    if (x < 0.0d0) then
      v = 0.0d0
    else
      v = 5.0d0
    end if
  end function step_potential

  function stepped_trap(x) result(v)                                         ! Step with right 'wall'
    implicit none
    real(8), intent(in) :: x                                                 ! Position
    real(8) :: v                                                             ! Potential value
    if (x < 0.0d0) then
      v = 0.0d0                                                              ! Flat potential on left
    else if (x >= 0.0d0 .and. x < 3.0d0) then
      v = 5.0d0                                                              ! Step region (E < V -> decay)
    else
      v = 1.0d6                                                              ! High wall to confine system (act as infinity)
    end if
  end function stepped_trap

  real(8) function step_barrier(x)
    implicit none
    real(8), intent(in) :: x

    if (x < 0.0d0) then
      step_barrier = 0.0d0
    else if (x <= 5.0d0) then
      step_barrier = 5.0d0
    else
      step_barrier = 0.0d0
    end if
  end function step_barrier



end module potential_functions                                        ! End of whole module

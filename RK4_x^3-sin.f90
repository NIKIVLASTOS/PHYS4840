program RungeKutta4
    implicit none
    real(8) :: t, x, dt, k1, k2, k3, k4, t_end  ! Real numbers
    integer :: n, i                                ! Integer variables
    real(8) :: start_time, end_time, elapsed_time  ! Timing variables

    ! Define initial conditions
    t = 0.0d0      ! Initial time
    x = 1.0d0      ! Initial condition for x
    dt = 0.1d0     ! Time step
    t_end = 10.0d0 ! Final time
    
    ! Number of time steps
    n =  10000 !int((t_end - t) / dt)

    ! Start timing
    ! call cpu_time(start_time)

    ! Open a file to store results
    open(unit=10, file="rk4_resultsHW10000.dat", status="replace")
    write(10,*) "t x"
    
    ! Initialize t and x for the interval [0, 10]
    t = 0.0d0
    x = 1.0d0

    ! Output initial values to the file
    write(10,*) t, x

    ! RK4 integration loop
    do i = 1, n
        k1 = dt * (-x**3 + sin(t))                         ! f(x, t) = -x^3 + sin(t)
        k2 = dt * (-(x + 0.5d0 * k1)**3 + sin(t + 0.5d0 * dt))
        k3 = dt * (-(x + 0.5d0 * k2)**3 + sin(t + 0.5d0 * dt))
        k4 = dt * (-(x + k3)**3 + sin(t + dt))

        ! Update the solution
        x = x + (1.0d0 / 6.0d0) * (k1 + 2.0d0 * k2 + 2.0d0 * k3 + k4)
        t = t + dt

        ! Write results to file
        write(10,*) t, x
    end do

    ! Stop timing
    ! call cpu_time(end_time)
    ! elapsed_time = end_time - start_time

    ! Close the file
    close(10)

    ! Print execution time
    print *, "Integration complete. Results saved to rk4_resultsHW10000.dat"
    ! print *, "Execution time (seconds):", elapsed_time

end program RungeKutta4


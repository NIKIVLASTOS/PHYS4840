program RungeKutta2        
    implicit none
    real(8) :: t, x, dt, k1, k2, t_end     
    integer :: n, i                        
    real(8) :: start_time, end_time, elapsed_time  ! Variables for timing

    ! Define initial conditions
    t = 0.0d0      
    x = 1.0d0      
    dt = 0.1d0     
    t_end = 10.0d0 
    
    ! Number of time steps
    n = int((t_end - t) / dt) 

    ! Start timing
    call cpu_time(start_time)  

    ! Open a file to store results
    open(unit=10, file="rk2_resultsHW.dat", status="replace")
    write(10,*) "t x"
    write(10,*) t, x
    
    ! RK2 integration loop
    do i = 1, n
        k1 = dt * (-x**3 + sin(t))  ! First stage of RK2
        k2 = dt * (-(x + 0.5d0*k1)**3 + sin(t + 0.5d0*dt))  ! Second stage of RK2
        
        x = x + k2  ! Update the value of x
        t = t + dt  ! Update the time
        
        ! Write results to file
        write(10,*) t, x
    end do

    ! Stop timing
    call cpu_time(end_time)
    elapsed_time = end_time - start_time

    ! Close file
    close(10)

    ! Print execution time
    print *, "Integration complete. Results saved to rk2_resultsHW.dat"
    print *, "Execution time (seconds):", elapsed_time

end program RungeKutta2

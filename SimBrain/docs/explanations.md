
# This is an advanced explanation of some parts of the SimBrian library

-----  

## CalculateFor()

The purpose of calculate for is to find the solution to the calculations using the user's variables stored in `particle_list` - the user calls the function as `calculateFor(index)` where index is the index of the experiment in particle_list.

> Within this function lies many subfunctions, such as:
> - `speeds_calculation` - to calculate the speeds of the particle at any given point
> - `hit_ground` - to identify when the particle hits the ground (this is one of the events in solve_ivp)
> - `z_max` - this identifies when the particle reaches its peak (another event in solve_ivp)
>  
> Each of these functions are crucial for the `solve_ivp` function called later.

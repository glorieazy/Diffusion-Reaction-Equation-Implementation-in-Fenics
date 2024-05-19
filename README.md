### Diffusion-Reaction-Equation-Implementation-in-Fenics

this repository discusses the implementation of the diffusion-reaction equation 
using fenics modules in python. 

NB: before implementation, make sure fenics is install on your machine (computer).

the equation is given by,
                  $\{-\kappa \Delta u + m u = f}$
where $\kappa > 0$ and $m > 0$.

We are solving on three different mesh sizes; 8x8, 16x16, 32x32, 64x64. So edit the code
accordingly to get result for each mesh size in line 13.

Also, we use piecewise linear and quadratic functions. this can be adjusted accordingly in 
line 16 of the python file by switching the values
         1 implies piecewise linear function
         2 implies piecewise quadratic function

###################################################################################
############ Kindly Read the ReadMe file before executing the code ################
###################################################################################

#import the necessary library
from fenics import *
import numpy as np
import matplotlib.pyplot as plt

k = m = 1

#generate a unit sqaure mesh
mesh = UnitSquareMesh(8, 8)

#define the finite element function space 
V = FunctionSpace(mesh, "P", 1) #Lagrange type family of degree 1 (linear)

#define the boundary condition
u_D = Expression("x[0]*x[0]*x[0] + x[1]*x[1]*x[1]", degree=3)

def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, u_D, boundary)

#specify trial and test functions
u = TrialFunction(V)
v = TestFunction(V)

#integrate the weak form of the PDE
f = Expression("x[0]*x[0]*x[0] + x[1]*x[1]*x[1] - 6.0 * x[0] -6.0 * x[1]", degree=3)
a = Constant(k)*dot(grad(u), grad(v))*dx + Constant(m)*u*v *dx
L = f*v*dx

#compute solution u by solving the problem a == L
u = Function(V)
solve(a==L, u, bc)

#compute error norm
error_L2 = errornorm(u_D, u, "L2")
#compute infinity error norm
vertex_values_u_D = u_D.compute_vertex_values(mesh)
vertex_values_u = u.compute_vertex_values(mesh)
error_max = np.max(np.abs(vertex_values_u_D - vertex_values_u))

#print error result
print("error_L2 = ", error_L2)
print("error_max = ", error_max)

plot(u)
plot(mesh)
plt.show()

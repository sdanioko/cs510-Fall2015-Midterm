# cs510-Fall2015-Midterm

Midterm : " Euler and Runga Kutta "

 * Brief description of the  Euler's Method
   Euler's method is a straight-forward first order method that estimates the next point based on the rate of change at 
   the current point. Euler's method is mainly baed on approximating the graph of a solution with a sequence of tangeante
   approximations computed sequentially in setps. 
       
 * Brief description of the Runge  Kutta's Methods
   They are a general class of alogrithms, with the fourth order one being the most famous one,  that actually shoot for
   an imporvement over the rather simple Euler's method despite that they use it as a basis. 
   
 
 
 Despite a very noticable similarity between the two methods, the Runge kutta Method uses parabolas(of 2nd order) and quadratic
 curves( of 4th order) as springboards in order to achieve better approximations.

 This project aims at investigating the Euler and the Runge Kutta Methods; two well known techniques for solving systems
 of differential equations. For, study we have investigated the effects of some parameters, such as the initial conditions,
 the time step size, the choice of the icrement on the solutions of a given system of differential equations.
 
 From this project, we can retain  that : 1-  Despite that the euler methode being very simple to be implimented, it just 
 provide a very shallow approach to the desired solutions of a system of differential of equation. 
 2- The Runge kutta a much better approach than the euler method. 3- Decreasing the time step maximes the chance to obtain
 convergence. 4- It is very difficult to conduct some analyses on the x, y, and z plots due to the chaotic features they
 display. 5- The choice of the initial conditions should be miticulously done in order to avoid eventual pertubations or 
 chaotic situations.
 
 To conduct this project; three main files were extensively used :
 
     a- Attractor.ipynb :  This file contains the Data Type Attractor, which in its turns contains the default constructor;
        the rhs, euler, rk2, rk4, save, plotx, ploty, plotz, and plot3d
     b- test_attractor.py : This file is used to verify a single minimal unit of source of code. It serves for isolating and 
        testing the smallest part of our Attractor class in order to see whether or not the above methods are functioning 
        perfectly in isolation. This help us make sure whether or not the methods listed above operate as they were to function,
        crash and continue to work on invalide data
     c- Explorer Attractor.ipynb : This file displays the empirical results obtained from 

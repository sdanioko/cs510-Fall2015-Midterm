import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D



class Attractor:
    """ The Attractor class is a Data Type that provides us ways of investigating Euler and Runge Kutta Methods """

    def __init__(self, s=10.0, p=28.0, b=8.0/3.0, start=0, end=80.0, points=10000):
        ''' Initialize attractor with the parameters s, p, b.
            Integration space is set by start and end.
            Integration step is controlled by the number of points
            which is also set as a parameter.
        '''
        self.params = np.array([s, p, b])
        self.start = start
        self.end = end
        self.points = points
        self.dt = (end - start)/points

    def rhs(self, xyz_arr):
        ''' Computes the right hand side of the system of equations
            that represents the attractor base on the current values
            of integrated variables
        '''
        # In here,let's unpack the data values
        x0, y0, z0 = xyz_arr
        s, p, b = self.params
        # the right-hand side of the dynamical equation
        x =  s * (y0 - x0)
        y = x0 * (p - z0) - y0
        z = x0 * y0 - b * z0
        # In here, we will be returning the packed value
        return np.array([x, y, z])


    def euler(self, xyz_arr):
        ''' Evolve a single integration step using 
            1st order Euler scheme
        '''

        k1 = xyz_arr + self.rhs(xyz_arr) * self.dt

        return k1

    def rk2(self, xyz_arr):
        ''' Evolve a single integration step using
            second order Runge-Kutta scheme
        '''
        k1 = self.rhs(xyz_arr)
        k2 = self.rhs(xyz_arr + k1 * self.dt / 2.0)

        return xyz_arr + k2 * self.dt


    def rk4(self, xyz_arr):
        ''' Evolve a single integration step using 
            fourth order Runge-Kutta scheme
        '''
        k1 = self.rhs(xyz_arr)
        k2 = self.rhs(xyz_arr + k1 * self.dt / 2.0)
        k3 = self.rhs(xyz_arr + k2 * self.dt / 2.0)
        k4 = self.rhs(xyz_arr + k3 * self.dt)

        return xyz_arr + self.dt / 6.0 * (k1 + 2*k2 + 2*k3 + k4)

    def evolve(self, r0=np.array([0.1, 0.0, 0.0]), order=4):
        ''' Evolve the whole system using an array of initial 
            values r0 with the method that correspond to the 
            selected order of integration
        '''
        # select an integrator #
        if order == 1:
            increment = self.euler
        elif order == 2:
            increment = self.rk2
        elif order == 4:
            increment = self.rk4
        else:
            print('No itegrator of order {0} found'.format(order))
            return None

        # In here, let's create a dict of data arrays
        data_dict = {k: np.zeros(self.points) for k in 'txyz'}
        self.solution = pd.DataFrame(data_dict)
        xyz = r0 # initalize
        for i in range(self.points):
            x, y, z = xyz
            self.solution.loc[i] = [i*self.dt, x, y, z]
            # This allows us to have time advance
            xyz = increment(xyz)

        return self.solution


    def save(self, filename):
        ''' Write solution arrays to csv file
        '''
        self.solution.to_csv(filename, index=False)


    def plotx(self): 
        ''' Display x vs t plot
        '''
        pl.ylabel('x (t)') # label the y axis as x(t)
        pl.xlabel('t') # label the x axis as t
        pl.plot(self.solution['t'], self.solution['x'], '-', color='r') # plot the column x of soultion vs its column t
        pl.show() # at the end call show to ensure window won't close.

    def ploty(self):
        ''' Display y vs t plot
        '''
        pl.ylabel('y (t)')
        pl.xlabel('t')
        pl.plot(self.solution['t'], self.solution['y'], '-', color='g')
        pl.show()  # at the end call show to ensure window won't close.

    def plotz(self):
        ''' Display z vs t plot
        '''
        pl.ylabel('z (t)')
        pl.xlabel('t')
        pl.plot(self.solution['t'], self.solution['z'], '-', color='b')
        pl.show()  # at the end call show to ensure window won't close.

    def plotxy(self):
        ''' Display y vs x
        '''
        pl.ylabel('y(t)')
        pl.xlabel('x(t)')
        pl.plot(self.solution['x'], self.solution['y'])
        pl.show() # at the end call show to ensure window won't close.

    def plotyz(self):
        ''' Display z vs y
        '''
        pl.xlabel('y(t)')
        pl.ylabel('z(t)')
        pl.plot(self.solution['y'], self.solution['z'])
        pl.show() # at the end call show to ensure window won't close.

    def plotzx(self):
        ''' Display x vs z
        '''
        pl.xlabel('z(t)')
        pl.ylabel('x(t)')
        pl.plot(self.solution['z'], self.solution['x'])
        pl.show() # at the end call show to ensure window won't close.

    def plot3d(self):
        ''' Display the 3d plot of the solution
        '''
        ax = pl.gca(projection='3d')
        pl.plot(self.solution['x'], self.solution['y'], self.solution['z'])
        pl.show() # at the end call show to ensure window won't close.


if __name__ == '__main__':
    " saple plot with default values "
    a = Attractor()
    a.evolve()
    a.plot3d()
    
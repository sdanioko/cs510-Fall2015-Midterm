" This file helps us test the different methods we built up in our Attractor"

import os
import numpy as np
from attractor import Attractor


def test_dt_value():
    ''' Ensure that dt is calculated as it is supposed to be
    '''
    a = Attractor()
    assert a.end == a.dt * a.points, "\n time step is not properly evaluated \n"

def test_rhs_shape():
    ''' Validate that the shape of the rhs method return value
    '''
    a = Attractor()
    xyz = np.array([0.0, 0.0, 0.0])
    assert a.rhs(xyz).shape == (3, ), "\n the shape of the array that was returned is not 3 \n"

def test_euler_shape():
    ''' Validate that the shape of the euler method return value
    '''
    a = Attractor()
    xyz = np.array([0.0, 0.0, 0.0])
    assert a.euler(xyz).shape == (3, ), "\n the shape of the array that was obtained from euler is not 3 \n"

def test_rk2_shape():
    ''' Validate that the shape of rk2 method return value
    '''
    a = Attractor()
    xyz = np.array([0.0, 0.0, 0.0])
    assert a.rk2(xyz).shape == (3, ), "\n the shape of the array that was obtained from rk2 is not 3 \n"

def test_rk4_shape():
    ''' Validate that the shape of rk4 method return value
    '''
    a = Attractor()
    xyz = np.array([0.0, 0.0, 0.0])
    assert a.rk4(xyz).shape == (3, ), "\n the shape of the array that was obtained from rk4 is not 3 \n"

def test_evolve_shape():
    ''' Validate that the shape of evolve method return value
    '''
    a = Attractor()
    assert a.evolve().shape == (a.points, 4), "\n the array that was obtained does not have a proper shape \n"
def test_save_csv():
    ''' Ensure that the csv file is created
    '''
    filename = 'filename.csv'
    a = Attractor()
    os.remove(filename)
    a.evolve()
    a.save(filename)
    assert os.path.exists(filename), "\n no output file found \n"
    print(" test_save_csv method is working as expected ")
" This file helps us test the different methods we built up in our Attractor"

import os
import numpy as np
from attractor import Attractor


def test_dt_value():
    " Let's ensure that dt is calculated as it is supposed to be "
    a = Attractor()
    assert a.end == a.dt * a.points
def test_rhs_shape():
    " Let's see how to validate the shape of rhs method return value "
    a = Attractor()
    xyz = np.array([0.0, 0.0, 0.0])
    assert a.rhs(xyz).shape == (3, )
def test_euler_shape():
    " Let's see how to validate the shape of euler method return value"
    a = Attractor()
    xyz = np.array([0.0, 0.0, 0.0])
    assert a.euler(xyz).shape == (3, )
def test_rk2_shape():
    " Let's see how to validate the shape of rk2 method return value "
    a = Attractor()
    xyz = np.array([0.0, 0.0, 0.0])
    assert a.rk2(xyz).shape == (3, )
def test_rk4_shape():
    " Let's see how to validate the shape of rk4 method return value "
    a = Attractor()
    xyz = np.array([0.0, 0.0, 0.0])
    assert a.rk4(xyz).shape == (3, )
def test_evolve_shape():
    " Let's how to validate the shape of evolve method return value " 
    a = Attractor()
    assert a.evolve().shape == (a.points, 4)
def test_save_csv():
    " Let's ensure that csv file is created "
    filename = 'test_cvs_filename.csv'
    a = Attractor()
    os.remove(filename)
    a.evolve()
    a.save(filename)
    assert os.path.exists(filename)
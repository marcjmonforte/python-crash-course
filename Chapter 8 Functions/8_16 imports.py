"""
8-16 Imports: Using a program you wrote that has one function in it,
store that function in a separate file. Import the function into your
main program file, and call the function using each of these
approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn 
import module_name as mn 
from module_name import *
"""

import test_function
test_function.dummy_function()

from test_function import dummy_function
dummy_function()

from test_function import dummy_function as df
df()

import test_function as tf
tf.dummy_function()

from test_function import *
dummy_function()
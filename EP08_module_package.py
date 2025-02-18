import numpy
import matplotlib.pyplot as plt

from my_package import greet, multiply_numbers
from my_package import farewell as fw


greet("jace")
fw("jace2")

multiply_numbers(2,4)


x = numpy.linspace(0,10,100):

plt.plot(*args:x, numpy.sin(x), label='sine', color='blue')
plt.show()


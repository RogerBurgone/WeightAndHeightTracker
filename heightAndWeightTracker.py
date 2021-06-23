""" displays graphs of kids weight and height compared to WHO averages"""

import matplotlib.pyplot as plt
import pandas as pd

HeightMales = pd.read_csv (r'Height Males_Ages 2-20 Years.csv',sep=';')
# print(HeightMales)

HeightMales.plot(kind='scatter',x='Age',y='3rd',color='red')

#
#
# #example from python book
# numbers=range(1,5001)
# cubes=[x**3 for x in numbers]
#
# #scatter plot
# plt.scatter(numbers, cubes, color=(0,0.85,0.85), edgecolor='none', s=100)
# #plt.scatter(numbers, cubes, c='green', s=100)
#
# #line plot
# #plt.plot(numbers, cubes, linewidth=5)
#
#
# #config axis and title
# plt.title("Cubic numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Cube of value", fontsize=14)
#
# #set the size of axis values and then the range
# plt.tick_params(axis='both', labelsize=14)
# plt.axis([0,5001,0,110000000000])
#
# plt.show()

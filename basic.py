# Mean - The average value
# Median - The mid point value
# Mode - The most common value
# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.
# Percentiles are used to give a number that describes the value that a given percent of the values are lower than.
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = np.mean(speed)
median = np.median(speed)
mode = stats.mode(speed)
sd = np.std(speed)
print(f"The mean(avg value) of speed list is {mean}")
print(f"The median(mid point value) of speed list is {median}")
print(f"The mode(most common value) of speed list is {mode}")
print(f"The sd(spreaded value are) of speed list is {sd}")

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
# percntile = np.percentile(ages, 75)
# What is the age that 90% of the people are younger than?
percntile = np.percentile(ages, 90)
print(f"Age percentile {percntile}")

# Create an array containing 250 random floats between 0 and 5:
x = np.random.uniform(0.0, 5.0, 250)
print(x)
plt.hist(x, 5)
plt.show()

largex = np.random.uniform(0.0, 5.0, 100000) #uniform data dist
# x = np.random.normal(5.0, 1.0, 100000) #normal data dist
plt.hist(x, 100)
plt.show()
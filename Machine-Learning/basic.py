import numpy
import scipy.stats as stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86,81,89]

# Mean
mean = numpy.mean(speed)
print('Mean is : ', mean)

# Median
median = numpy.median(speed)
print('Median is : ', median)

# Mode
mode = stats.mode(speed)
print('Mode is : ', mode)

deviation = numpy.std(speed)
print('Standard deviation is : ', deviation)

percentile = numpy.percentile(speed, 75)
print('Percentile is : ', percentile)
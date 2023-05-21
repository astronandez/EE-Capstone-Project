from importAgilentBin import *
from matplotlib import pyplot as plt

for i in range(100):
    time, data = readfile("C:/Users/march/Documents/EE 497-498/20230412jpl_capstone/tc99m/tc99m00000.bin", i)
    # Extract the data from the two columns
    x = time
    y = data

    # Create a line plot of the data
    plt.plot(x, y)
    plt.xlabel('Second')
    plt.ylabel('Volt')
    plt.title('Volts vs. Seconds')
    plt.show()
    

import pandas as pd
import matplotlib.pyplot as plt

# Create a Pandas Series with your data
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,2,3,4,5,5,4,4,5,5,5,6,7,6,7,6,6])
print(type(data))

# Calculate the cumulative distribution function (CDF) using quantiles
cdf = data.quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

# Create a plot of the CDF
plt.plot(cdf, cdf.index / len(data), marker='o', linestyle='-')

# Label the axes
plt.xlabel('Value')
plt.ylabel('CDF')

# Show the plot
plt.show()
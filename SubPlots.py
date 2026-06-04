import numpy as np
import matplotlib.pyplot as plt

# Generating sample data
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y = np.sin(x)

fig , axs = plt.subplots(2,2,figsize=(10,10))

# Line chart
axs[0,0].plot(x,y,color='red',linewidth=2)
axs[0,0].set_xtricks=(range(0,11,1))
plt.xticks.rotation=30
axs[0,0].set_title('Line Chart')

# Scatter plot
axs[0,1].scatter(x,y,color='blue')
axs[0,1].set_title('Scatter Plot')

# Histogram
axs[1,0].hist(np.random.randn(100), bins=20, color='green')
axs[1,0].set_title('Histogram')

# Bar chart
Category = ['Electronics','Clothing','Books','Home & Kitchen']
Values = [10,20,30,40]
axs[1,1].bar(Category,Values, color='indigo')
axs[1,1].set_title('Bar Chart')

plt.tight_layout()
plt.show()


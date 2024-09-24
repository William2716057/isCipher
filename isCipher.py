import matplotlib.pyplot as plt
import numpy as np

letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]  
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


plt.bar(letters, values, color='blue')


plt.title('Expected letter frequences')
plt.xlabel('Letters')
plt.ylabel('Frequences')

# Show grid
plt.grid(axis='y')

# Display the plot
plt.show()
plt.show()

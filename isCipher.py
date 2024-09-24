import matplotlib.pyplot as plt
import numpy as np

letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]  
values = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]

plt.bar(letters, values, color='blue')

plt.title('Expected letter frequences')
plt.xlabel('Letters')
plt.ylabel('Frequences')

plt.grid(axis='y')

plt.show()


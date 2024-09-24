import matplotlib.pyplot as plt
import numpy as np

letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]  
values = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]

#plt.bar(letters, values, color='blue')

#.title('Expected letter frequences')
#plt.xlabel('Letters')
#plt.ylabel('Frequences')

#plt.grid(axis='y')

#plt.show()

def letter_occurrences_percentage(input_string):

    filtered_string = ''.join(filter(str.isalpha, input_string.lower()))
    
    total_letters = len(filtered_string)
    
    letter_count = {}
    for letter in filtered_string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    letter_percentage = {letter: (count / total_letters) * 100 for letter, count in letter_count.items()}

    return letter_percentage

input_string = "This is a long string with repeated letters in to see the percentage of each letter that is written. A longer sentence is probably better"
percentages = letter_occurrences_percentage(input_string)


second_values = [percentages.get(letter, 0) for letter in letters] 

x = np.arange(len(letters))

width = 0.4  # width
plt.figure(figsize=(12, 6))
plt.bar(x - width/2, values, width, color='blue', label='Expected Frequencies')
plt.bar(x + width/2, second_values, width, color='red', label='Sample frequencies')


plt.title('Letter Frequency Comparison')
plt.xlabel('Letters')
plt.ylabel('Frequencies (%)')
plt.grid(axis='y')

plt.legend()

# Show the second plot
plt.show()
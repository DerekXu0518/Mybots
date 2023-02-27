import matplotlib.pyplot as plt

# Define a list of file names to read in
file_names = ['OverallFitness0.txt']

# Initialize an empty list to store the data from all files
all_data = []

# Loop over each file and read in the data
for file_name in file_names:
    with open(file_name, 'r') as file:
        data = []
        for line in file:
            row = [float(x) for x in line.split()]
            data.append(row)
        all_data.append(data)

# Initialize an empty list to store the maximum values from all files
all_max_values = []

# Loop over each set of data and find the maximum value for each sublist
for data in all_data:
    max_values = []
    for sublist in data:
        max_value = max(sublist)
        max_values.append(max_value)
    all_max_values.append(max_values)

# Plot all the maximum values in one plot
for i, max_values in enumerate(all_max_values):
    plt.plot(range(1, len(max_values) + 1), max_values, label=f'Run {i+1}')

plt.xlabel('Generations')
plt.ylabel('Best Fitness')
plt.title('Fitness curve')
#plt.xticks(range(1, len(max_values) + 1))
plt.legend()
plt.show()

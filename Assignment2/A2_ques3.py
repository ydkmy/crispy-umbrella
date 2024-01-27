#Prepare a dictionary from file3.txt.
# Initialize an empty dictionary to store the key-value pairs
data_dict = {}

with open('file3.txt', 'r') as file:

    for line in file:

        key, value = line.strip().split(',')

        data_dict[key] = value

print(data_dict)

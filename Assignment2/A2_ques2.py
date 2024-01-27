#Convert all the numbers in the file2.txt to text. 
#Ex: This file has numbers 1,2
#Convert it to : This file has numbers one,two
# Define a function to convert numbers to text
def convert_numbers_to_text(content):
    number_to_text = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    for digit in number_to_text:
        content = content.replace(digit, number_to_text[digit])

    return content

with open('file2.txt', 'r') as file:
    file_contents = file.read()

converted_content = convert_numbers_to_text(file_contents)

print(converted_content)

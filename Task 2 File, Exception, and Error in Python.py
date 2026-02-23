'''
Write a Python program that: 
1. Takes user input and writes it to a file named output.txt. 
2. Appends additional data to the same file. 
3. Reads and displays the final content of the file.
'''

# 1. Take user input and write it to output.txt
data = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

# 2. Append additional data to the same file
more_data = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(more_data + "\n")

# 3. Read and display the final content of the file
print("\nFinal content of the file:")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)

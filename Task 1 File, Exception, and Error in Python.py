# Program to read a file and handle errors
# 1. Open and read the file
# 2. Print content line by line
# 3. Handle error if file does not exist


try:
    # 1. Open and read the file
    with open("sample.txt", "r") as file:
        
        # 2. Print content line by line
        for line in file:
            print(line.strip())

except FileNotFoundError:
    # 3. Handle error if file does not exist
    print("Error: The file 'sample.txt' does not exist.")

except Exception as e:
    print("An unexpected error occurred:", e)

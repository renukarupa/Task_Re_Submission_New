def read_text_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            file_content = file.read()
            # Display the content in the console
            print(f"Content of '{filename}':\n{file_content}")
    except FileNotFoundError:
        # Handle the case when the file is not found
        print(f"Error: File '{filename}' not found.")

# Call the function with the filename as an argument
read_text_file("current timestamp.txt")

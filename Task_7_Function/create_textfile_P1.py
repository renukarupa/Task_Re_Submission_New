import datetime
def create_timestamp_file():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Define the filename with the current timestamp
    filename = f"current timestamp{current_timestamp}.txt"

    # Open the file in write mode and write the current timestamp as content
    with open(filename, 'w') as file:
        file.write(current_timestamp)

    print(f"File '{filename}' created with content: {current_timestamp}")


# Call the function to create the timestamp file
create_timestamp_file()

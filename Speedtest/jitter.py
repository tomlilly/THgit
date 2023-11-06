# Import the pandas library
import pandas as pd

# Define a function to extract information from a file
def extract_info(file_name):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read all lines from the file
        data = file.readlines()

    # Initialize an empty list to store the records
    records = []
    # Initialize an empty dictionary to store a record
    record = {}
    # Initialize a variable to keep track of the jitter information
    jitter_info = False
    # Iterate over each line in the data
    for line in data:
        # Remove leading and trailing whitespaces from the line
        line = line.strip()
        # Check if the line starts with 'Speedtest by Ookla'
        if line.startswith('Speedtest by Ookla'):
            # If there is a record, append it to the records list
            if record:
                records.append(record)
            # Start a new record
            record = {}
        # Check if the line starts with 'Server:'
        elif line.startswith('Server:'):
            # Extract the server information and add it to the record
            record['Server'] = line.split(' - ')[1]
        # Check if the line starts with 'ISP:'
        elif line.startswith('ISP:'):
            # Extract the ISP information and add it to the record
            record['ISP'] = line.split(': ')[1]
        # Check if the line starts with 'Idle Latency:'
        elif line.startswith('Idle Latency:'):
            # If the line contains jitter information
            if ' (jitter: ' in line:
                # Extract the jitter, low, and high information and add them to the record
                record['Idle_jitter'], record['Idle_low'], record['Idle_high'] = line.split(' (jitter: ')[1].split(', ')
                # Remove the closing parenthesis from the high information
                record['Idle_high'] = record['Idle_high'].replace(')', '')
        # Check if the line starts with 'Download:'
        elif line.startswith('Download:'):
            # Extract the download information and add it to the record
            record['Download'] = line.split(': ')[1]
            # Set the jitter information to 'Download'
            jitter_info = 'Download'
        # Check if the line starts with 'Upload:'
        elif line.startswith('Upload:'):
            # Extract the upload information and add it to the record
            record['Upload'] = line.split(': ')[1]
            # Set the jitter information to 'Upload'
            jitter_info = 'Upload'
        # If there is jitter information
        elif jitter_info:
            # Extract the jitter, low, and high information and add them to the record
            record[jitter_info + '_jitter'], record[jitter_info + '_low'], record[jitter_info + '_high'] = line.split(' (jitter: ')[1].split(', ')
            # Remove the closing parenthesis from the high information
            record[jitter_info + '_high'] = record[jitter_info + '_high'].replace(')', '')
            # Reset the jitter information
            jitter_info = False
        # Check if the line contains a date and time
        elif len(line.split('/')) == 3 and len(line.split(':')) == 3:
            # Add the date and time to the record
            record['Date'] = line
    # If there is a record, append it to the records list
    if record:
        records.append(record)

    # Convert the records list into a pandas DataFrame
    df = pd.DataFrame(records, columns=['Date', 'Server', 'ISP', 'Idle_jitter', 'Idle_low', 'Idle_high', 'Download_jitter', 'Download_low', 'Download_high', 'Upload_jitter', 'Upload_low', 'Upload_high'])
    # Write the DataFrame to an Excel file
    df.to_excel('output.xlsx', index=False)

# Call the function with the file name as argument
extract_info('speedtest.txt')
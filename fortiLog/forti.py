import pandas as pd
import re

# Initialize an empty list to store the data
data = []

# Open the log file
with open('fortiLog.log', 'r') as file:
    for line in file:
        # Check if the line contains "terminated"
        if "terminated" in line:
            # Split the line into components
            components = line.split()
            # Extract the date, time (including AM/PM)
            date = components[0]
            time = components[1] + ' ' + components[2]
            # Extract the event description, ignoring "info", "update", and "sslvpn"
            event_description = ' '.join([comp for comp in components[3:] if comp not in ["info", "update", "sslvpn"]])
            # Append the data to the list
            data.append([date, time, event_description])

# Convert the list to a DataFrame
df = pd.DataFrame(data, columns=['Date', 'Time', 'Event Description'])

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
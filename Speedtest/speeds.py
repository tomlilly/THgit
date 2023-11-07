import pandas as pd
import re

# Initialize lists to store data
dates, times, servers, isps, downloads, uploads = [], [], [], [], [], []

# Open and read the file
with open('speedtest.txt', 'r') as file:
    lines = file.readlines()

# Loop over the lines and extract the data
for line in lines:
    if re.search(r'\d{2}/\d{2}/\d{4}', line):
        _, date, time = line.strip().split(maxsplit=2)
        dates.append(date)
        times.append(time)
    elif 'Server:' in line:
        server = line.split(': ')[1].strip()
        servers.append(server)
    elif 'ISP:' in line:
        isp = line.split(': ')[1].strip()
        isps.append(isp)
    elif 'Download:' in line:
        download = line.split()[1]
        downloads.append(download)
    elif 'Upload:' in line:
        upload = line.split()[1]
        uploads.append(upload)

# Create a DataFrame from the lists
df = pd.DataFrame({
    'Date': dates,
    'Time': times,
    'Server': servers,
    'ISP': isps,
    'Download': pd.to_numeric(downloads),
    'Upload': pd.to_numeric(uploads)
})

# Write the DataFrame to an Excel file
df.to_excel('speedtest.xlsx', index=False)
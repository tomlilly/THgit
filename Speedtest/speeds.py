import pandas as pd
import re

# Initialize lists to store data
dates = []
servers = []
isps = []
downloads = []
uploads = []

# Open and read the file
with open('speedtest.txt', 'r') as file:
    lines = file.readlines()

# Loop over the lines and extract the data
for line in lines:
    if re.search(r'\d{2}/\d{2}/\d{4}', line):
        date = re.search(r'\d{2}/\d{2}/\d{4}', line).group()
        dates.append(date)
    elif 'Server:' in line:
        server = line.split('Server:')[1].strip()
        servers.append(server)
    elif 'ISP:' in line:
        isp = line.split('ISP:')[1].strip()
        isps.append(isp)
    elif 'Download:' in line:
        download = re.search(r'\d+\.\d+', line).group()
        downloads.append(download)
    elif 'Upload:' in line:
        upload = re.search(r'\d+\.\d+', line).group()
        uploads.append(upload)

# Create a DataFrame from the lists
df = pd.DataFrame({
    'Date': dates,
    'Server': servers,
    'ISP': isps,
    'Download': downloads,
    'Upload': uploads
})

# Write the DataFrame to an Excel file
df.to_excel('speedtest_data.xlsx', index=False)
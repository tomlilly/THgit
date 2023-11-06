import pandas as pd

def extract_info(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()

    records = []
    record = {}
    jitter_info = False
    for line in data:
        line = line.strip()
        if len(line.split('/')) == 3 and len(line.split(':')) == 3:
            if record:
                records.append(record)
            record = {'Date': line}
        elif line.startswith('Server:'):
            record['Server'] = line.split(' - ')[1]
        elif line.startswith('ISP:'):
            record['ISP'] = line.split(': ')[1]
        elif line.startswith('Idle Latency:'):
            if ' (jitter: ' in line:
                record['Idle_jitter'], record['Idle_low'], record['Idle_high'] = line.split(' (jitter: ')[1].split(', ')
                record['Idle_high'] = record['Idle_high'].replace(')', '')
        elif line.startswith('Download:'):
            record['Download'] = line.split(': ')[1]
            jitter_info = 'Download'
        elif line.startswith('Upload:'):
            record['Upload'] = line.split(': ')[1]
            jitter_info = 'Upload'
        elif jitter_info:
            record[jitter_info + '_jitter'], record[jitter_info + '_low'], record[jitter_info + '_high'] = line.split(' (jitter: ')[1].split(', ')
            record[jitter_info + '_high'] = record[jitter_info + '_high'].replace(')', '')
            jitter_info = False
    if record:
        records.append(record)

    df = pd.DataFrame(records, columns=['Date', 'Server', 'ISP', 'Idle_jitter', 'Idle_low', 'Idle_high', 'Download_jitter', 'Download_low', 'Download_high', 'Upload_jitter', 'Upload_low', 'Upload_high'])
    df.to_excel('output.xlsx', index=False)

extract_info('speedtest - 15m.txt')
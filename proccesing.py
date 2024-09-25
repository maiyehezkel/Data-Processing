import pandas as pd
import json

#Load the JSON log file
with open('example_file.json', 'r') as file:
    data = [json.loads(line) for line in file]

#Extract fields directly into a DataFrame
log_data = [
    {
        'Timestamp': entry.get('@timestamp'),
        'Application': entry.get('application'),
        'Agent': entry.get('agent', {}).get('name'),
        'Log File Path': entry.get('log', {}).get('file', {}).get('path'),
        'DateTime': entry.get('processed', {}).get('DateTime'),
        'Severity': entry.get('processed', {}).get('Severity'),
        'Thread': entry.get('processed', {}).get('Thread'),
        'Message': entry.get('processed', {}).get('message'),
        'ElementVersion': entry.get('processed', {}).get('ElementVersion'),
        'LineNumber': entry.get('processed', {}).get('LineNumber')
    }
    for entry in data
]

df = pd.DataFrame(log_data)

with pd.ExcelWriter('log_layers.xlsx', engine='openpyxl') as writer:
    #1.Raw Data Layer
    df.to_excel(writer, sheet_name='Raw Data', index=False)

    #2.Remove Duplicates based on 'Timestamp', 'Agent', and 'Application'
    df_no_duplicates = df.drop_duplicates(subset=['Timestamp', 'Agent', 'Application'])
    df_no_duplicates.to_excel(writer, sheet_name='No Duplicates', index=False)

    #3.Aggregated Data by Process Severity
    for severity, df_severity in df.groupby('Severity'):
        # Handle any rows with missing severity
        if pd.isna(severity):
            severity = 'Undefined'
        df_severity.to_excel(writer, sheet_name=f'{severity} Data', index=False)

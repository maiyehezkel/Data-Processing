# Log Data Processing and Excel Export Script

This Python script processes a JSON log file, extracts relevant fields into a Pandas DataFrame, removes duplicates based on specific columns, and exports the data into multiple sheets of an Excel file. The script provides different layers of log data processing, including raw data, deduplicated data, and aggregated data by severity.

## Requirements

To run this script, you'll need the following Python libraries installed:

- `pandas`
- `openpyxl`

You can install these packages using `pip`:

```bash
pip install pandas openpyxl
```

## Script Overview

### 1. **Loading JSON Log Data**

The script reads a JSON log file, where each line is a JSON object. It extracts the following fields into a Pandas DataFrame:

- `@timestamp`: The timestamp of the log entry.
- `application`: The application generating the log.
- `agent`: The name of the agent that generated the log.
- `log.file.path`: The file path of the log.
- `processed.DateTime`: The processed timestamp of the log.
- `processed.Severity`: The severity of the log entry (e.g., `ERROR`, `INFO`).
- `processed.Thread`: The thread that generated the log.
- `processed.message`: The log message.
- `processed.ElementVersion`: The version of the system element that generated the log.
- `processed.LineNumber`: The line number in the code where the log was generated.

### 2. **Excel Export**

The script exports the processed log data into an Excel file (`log_layers.xlsx`) with the following sheets:

- **Raw Data**: This sheet contains all the log data extracted from the JSON file without any filtering.
  
- **No Duplicates**: This sheet contains the log data after removing duplicate entries based on unique combinations of `Timestamp`, `Agent`, and `Application`.

- **Aggregated by Severity**: The script creates separate sheets for each log severity (e.g., `ERROR`, `INFO`, `WARN`). Each sheet contains the log entries corresponding to that severity. Rows with missing severity will be aggregated into an `Undefined` sheet.

### 3. **How to Run the Script**

1. Ensure your JSON log file is in the same directory as the script, or modify the file path accordingly.
   
2. Run the script:

```bash
python log_processing.py
```

3. After execution, the Excel file (`log_layers.xlsx`) will be generated in the current working directory.

### 4. **Customization**

- **Input File**: Modify the file path in the script to use a different JSON log file.
  
  ```python
  with open('example_file.json', 'r') as file:
  ```

- **Duplicate Criteria**: You can change the criteria for duplicate removal by modifying the subset passed to the `drop_duplicates` function:

  ```python
  df_no_duplicates = df.drop_duplicates(subset=['Timestamp', 'Agent', 'Application'])
  ```

- **Severity Handling**: If there are additional severities or you want different aggregation rules, you can customize the `groupby` logic.

### 5. **Known Limitations**

- The script expects the JSON file to have a specific structure. If the structure varies, you may need to adjust the `log_data` extraction logic.
- It handles missing severity by assigning those rows to an "Undefined" sheet.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For any issues or improvements, feel free to open an issue or contribute via pull requests.

---

This README provides a clear explanation of the script's functionality, usage instructions, and customization options. You can adjust it according to your specific use case or project structure.

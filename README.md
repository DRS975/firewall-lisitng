# firewall-lisitng

Certainly! Here's an updated version of the code that takes an input file containing firewall logs and writes the results (mentioning SQL injection vulnerabilities) to an output file:

```python
import re

# Function to check if a log entry contains SQL injection patterns
def check_sql_injection(log_entry):
    patterns = [
        r"(?i)\bunion\b",
        r"(?i)\band\b",
        r"(?i)\bor\b",
        r"(?i)\bselect\b",
        r"(?i)\binsert\b",
        r"(?i)\bupdate\b",
        r"(?i)\bdelete\b",
        r"(?i)\bdrop\b",
        r"(?i)\bexec\b",
        r"(?i)\btruncate\b",
        r"(?i)\balter\b",
        r"(?i)\bcreate\b",
        r"(?i)\bdeclare\b",
        r"(?i)\bwhere\b",
        r"(?i)\bcase\b"
        # Add more patterns as needed
    ]

    for pattern in patterns:
        if re.search(pattern, log_entry):
            return True

    return False

# Read firewall logs from a file
def read_firewall_logs(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

# Write results to an output file
def write_results(file_path, results):
    with open(file_path, 'w') as file:
        file.write(results)

# Main program
firewall_log_file = 'firewall_logs.txt'  # Path to the firewall log file
output_file = 'sql_injection_results.txt'  # Path to the output file

logs = read_firewall_logs(firewall_log_file)
results = ""

# Check for SQL injection patterns in each log entry
for log_entry in logs:
    if check_sql_injection(log_entry):
        results += "Potential SQL injection detected:\n"
        results += log_entry
        results += "-------------------------------------------------\n"

write_results(output_file, results)
print("Results written to", output_file)
```

In this updated code, we added a new function `write_results` that takes the output file path and the results as input, and writes the results to the output file.

The output file path is specified using the `output_file` variable. You can adjust it to your desired output file name and location.

After checking for SQL injection patterns in the log entries, the results are accumulated in the `results` string variable. Finally, the `write_results` function is called to write the results to the output file specified by `output_file`.

When you run this code, it will generate an output file (`sql_injection_results.txt`) containing the log entries that indicate potential SQL injection vulnerabilities.






import re

# Function to check if a log entry contains SQL injection patterns
def check_sql_injection(log_entry):
    patterns = [
        r"(?i)\bunion\b",
        r"(?i)\band\b",
        r"(?i)\bor\b",
        r"(?i)\bselect\b",
        r"(?i)\binsert\b",
        r"(?i)\bupdate\b",
        r"(?i)\bdelete\b",
        r"(?i)\bdrop\b",
        r"(?i)\bexec\b",
        r"(?i)\btruncate\b",
        r"(?i)\balter\b",
        r"(?i)\bcreate\b",
        r"(?i)\bdeclare\b",
        r"(?i)\bwhere\b",
        r"(?i)\bcase\b"
        # Add more patterns as needed
    ]

    for pattern in patterns:
        if re.search(pattern, log_entry):
            return True

    return False

# Read firewall logs from a file
def read_firewall_logs(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

# Write results to an output file
def write_results(file_path, results):
    with open(file_path, 'w') as file:
        file.write(results)

# Main program
firewall_log_file = 'firewall_logs.txt'  # Path to the firewall log file
output_file = 'sql_injection_results.txt'  # Path to the output file

logs = read_firewall_logs(firewall_log_file)
results = ""

# Check for SQL injection patterns in each log entry
for log_entry in logs:
    if check_sql_injection(log_entry):
        results += "Potential SQL injection detected:\n"
        results += log_entry
        results += "-------------------------------------------------\n"

write_results(output_file, results)
print("Results written to", output_file)

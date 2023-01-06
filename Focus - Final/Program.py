import subprocess

# Get a list of all running processes
processes = subprocess.run(["tasklist"], stdout=subprocess.PIPE).stdout.decode("utf-8").split("\r\n")

# Initialize the logged applications list
logged_applications = ['smartscreen.exe', 'Taskmgr.exe', 'firefox.exe','WerFault.exe', 'SearchProtocolHost.exe']

# Iterate through the list of processes
for process in processes:
    # Split the process line into fields
    fields = process.split()
    # Check if the fields list has at least 1 element
    if len(fields) > 0:
        # Add the process to the logged applications list
        logged_applications.append(fields[0])

while True:
    # Get a list of all running processes
    processes = subprocess.run(["tasklist"], stdout=subprocess.PIPE).stdout.decode("utf-8").split("\r\n")
    
    # Iterate through the list of processes
    for process in processes:
        # Split the process line into fields
        fields = process.split()
        # Check if the process is not in the whitelist
        if len(fields) > 0 and fields[0] not in logged_applications:
            # Terminate the process
            subprocess.run(["taskkill", "/F", "/IM", fields[0]])

print("All non-whitelisted processes have been terminated")

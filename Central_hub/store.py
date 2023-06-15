import csv, json, time


#time_threshold = 15780000       #6 months to retain data
time_threshold = 10

def data_store(sens_data, filename):
    field_names = ['Time', 'Temperature', 'Soil Moisture']
    load_data = json.loads(sens_data)
    
    with open(filename, mode='a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        for row in load_data:
            writer.writerow(row)

def data_clean(filename, time_threshold):
    clean_flag = False
    while not clean_flag:
        #Data delete after 
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
       
        oldest_timestamp = int(data[1][0])

        if time.time() - oldest_timestamp > time_threshold:
            del data[1]
            #field_names = ['Time', 'Temperature', 'Soil Moisture']

            with open(filename, 'w') as file:
                # headerwrite = csv.DictWriter(file, field_names)
                # headerwrite.writeheader()
                
                writer = csv.writer(file)
                writer.writerows(data)
        else:
            clean_flag = True

def nodeData(filename):
    with open(filename, 'r') as file:
        # Create a CSV reader object
        reader = csv.DictReader(file)
        entries = []

        # Iterate through the rows in reverse order, up to 24 rows
        for row in reversed(list(reader)):
            if len(entries) >= 24:
                break
            # Convert the row to a dictionary and add it to the entries list
            entries.append(dict(row))
    return entries

def dashboardData():
    heading = []
    # Loop through the two CSV files
    for file_id, filename in enumerate(['node1.csv', 'node2.csv'], 1):

        # Open the CSV file for reading
        with open(filename, 'r') as file:
            # Create a CSV reader object
            reader = csv.reader(file)

            # Get the last row in the CSV file
            last_row = None
            for row in reader:
                last_row = row

            # Create a dictionary from the last row and add the file id
            entry = {'Sensor_id': file_id, 'Time': last_row[0], 'Temperature': last_row[1], 'Soil Moisture': last_row[2]}

            # Add the dictionary to the data list
            heading.append(entry)
    return heading

def Fault_log(node_num, ch_sel, data_ack):
    print('Fault Logging ...')
    if not(data_ack and ch_sel) is True:
        # Open the CSV file for writing
        with open('fault_log.csv', mode='a', newline='') as csv_file:
            # Create a CSV writer object
            writer = csv.writer(csv_file)
            current_time = int(time.time())
            
            # Write the time and fault type to the CSV file
            writer.writerow([node_num, current_time, 'Fault: Channel Selection' if not ch_sel else 'Fault: Data Not Received'])

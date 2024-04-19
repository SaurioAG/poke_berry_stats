from datetime import datetime

def log_progress(message: str, log_file: str):
    """
    This function generates a txt faile that contains records with a timestamp for each stage of the process
    """
    print(message)
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    current_time = datetime.now() # get current timestamp 
    timestamp = current_time.strftime(timestamp_format)
    with open(log_file, "a") as logging_file:
        logging_file.write(timestamp + ',' + message + '\n')
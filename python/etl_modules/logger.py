from datetime import datetime

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format) 
    with open("./files/etl_project_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')
        
import os, datetime

path = '/Users/joelperry/Development/tabs'

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        dest_directory = os.path.join(path, str(time.year) + ' ' + time.strftime("%B"))

        if not os.path.isdir(dest_directory):
             os.makedirs(dest_directory)
        
        os.rename(file_path, os.path.join(dest_directory, file))
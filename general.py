import os

# Each website you scrape is a separate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

# Create queue and scraped files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + 'queue.txt'
    scraped = project_name + 'scraped.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(scraped):
        write_file(scraped, '')

# Writes a new files
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

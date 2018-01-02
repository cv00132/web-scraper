import os

# Each website you scrape is a separate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

create_project_dir('testproject')

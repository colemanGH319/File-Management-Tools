import tarfile
import sys
import os

def unzip_file(filename, dest='.'):
    if filename.endswith('.tar.gz'):
        file = tarfile.open(filename, "r:gz")
    elif filename.endswith('.gz'):
        file = tarfile.open(filename, "r:")
    file.extractall(path=dest)
    file.close()

if __name__ == '__main__':
    path_to_file, new_path = sys.argv[1], sys.argv[2]
    path_to_file = path_to_file.split('\\')
    path, filename = '\\'.join(path_to_file[:-1]), path_to_file[-1]
    os.chdir(path)
    unzip_file(filename, dest=(new_path if new_path else '.'))

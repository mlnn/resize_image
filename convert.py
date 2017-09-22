import os
import subprocess

source_path = 'Source'
result_path = 'Result'


def resize(files):
    for file in files:
        subprocess.run('convert {}/{} -resize 200 {}/{}'.format(source_path, file, result_path, file))


if __name__ == '__main__':
    files = os.listdir(path=source_path)
    os.mkdir('Result')
    resize(files)
    pass
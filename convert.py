import os
import subprocess
import time

start = time.time()
source_path = 'Source'
result_path = 'Result'


def resize(files):
    for file in files:
        subprocess.run('convert {} -resize 200 {}'.
                       format(os.path.join(source_path, file), os.path.join(result_path, file)))


if __name__ == '__main__':
    files = os.listdir(path=source_path)
    try:
        os.mkdir(result_path)
    except:
        print('Папка с результатами уже существует')
    resize(files)
    elapsed = (time.time() - start)
    print(elapsed)
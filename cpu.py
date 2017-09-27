from multiprocessing.dummy import Pool as ThreadPool
import os
import subprocess
import time

start = time.time()
source_path = 'Source'
result_path = 'Result'


def resize(files):
        subprocess.run('convert {} -resize 200 {}'.
                       format(os.path.join(source_path, files), os.path.join(result_path, files)))


if __name__ == '__main__':
    files = os.listdir(path=source_path)
    try:
        os.mkdir(result_path)
    except:
        print('Папка с результатами уже существует')
    pool = ThreadPool(4)
    pool.map(resize, files)
    pool.close()
    pool.join()
    elapsed = (time.time() - start)
    print(elapsed)


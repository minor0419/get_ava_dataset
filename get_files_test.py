import os
import subprocess

file_path1 = "./ava.txt"
file_path2 = "./ava_test.txt"
url1 = 'https://s3.amazonaws.com/ava-dataset/trainval/'
url2 = 'https://s3.amazonaws.com/ava-dataset/test/'

with open(file_path2, 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    url = url2 + line
    cmd = 'wget ' + '--no-clobber -q -P ./test ' + url
    print(cmd)
    subprocess.call(cmd, shell=True)

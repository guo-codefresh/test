#!/usr/bin/env python3
import os
import shutil


print('Hello World!')
# os.rename('/tmp/file.txt', 'dest.txt')
shutil.move('/tmp/file.txt', 'dest.txt')

#!/usr/bin/env python
import os
import shutil
import time


MBED_VOLUME_NAME = '/Volumes/MBED'


def is_new(file_path):
    return time.time() - os.path.getmtime(file_path) < 2.0


def is_bin_file(file_name):
    return os.path.splitext(file_name)[1] == '.bin'


def is_mbed_file(file_name):
    return 'KL25Z' in file_name


def copy_file(file_path):
    shutil.copy(file_path, MBED_VOLUME_NAME)


def delete_file(file_path):
    os.remove(file_path)


def is_mbed_mounted():
    return os.path.exists(MBED_VOLUME_NAME)


def watch_directory(directory_name=os.getcwd()):
    print 'Watching directory for MBED binaries..'
    try:
        while True:
            time.sleep(1)
            for file_name in os.listdir(directory_name):
                file_path = os.path.join(directory_name, file_name)
                if is_bin_file(file_name) and is_mbed_file(file_name) and is_new(file_path):
                    print 'Detected new mbed binary..'
                    if not is_mbed_mounted():
                        print 'MBED not mounted..'
                        break
                    print 'Copying file to MBED..'
                    copy_file(file_path)
                    delete_file(file_path)
                    print 'Waiting for new MBED binaries..'
                    break
    except KeyboardInterrupt as e:
        print '\nExiting!'


if __name__ == '__main__':
    watch_directory()

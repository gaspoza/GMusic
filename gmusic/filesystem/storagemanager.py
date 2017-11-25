from shutil import copyfile
import os
import os.path


class StorageManager:
    """
    StorageManager is the class handling the interaction with the filesystem
    """

    def __init__(self):
        pass

    @staticmethod
    def create_directory_if_not_existing(folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    @staticmethod
    def rename(src, dst):
        os.rename(src, dst)

    @staticmethod
    def has_file(path):
        return os.path.isfile(path)

    @staticmethod
    def copy_file(src, dst):
        if not os.path.isfile(src):
            raise ValueError('The file ' + src + 'not exist!')
        copyfile(src, dst)

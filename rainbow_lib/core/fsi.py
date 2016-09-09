"""A simple class for making interfacing with the file-system feel neater
"""

import os
import shutil

from .logging import logger


class FileSystemInterfacer(object):
    """A helper class for interfacing with the file system
    """

    def exists(self, path):
        logger.debug("[check-exists]:%s", path)
        return os.path.exists(path)

    def folder_create(self, folder_path, exist_ok=True):
        logger.debug("[ensure-exists-folder]: %s", folder_path)
        try:
            os.makedirs(folder_path, exist_ok=exist_ok)
        except FileExistsError as e:
            # Some Permissions related thing... Bleh.
            if e.errno != 17:
                raise

    def folder_delete(self, folder_path):
        logger.debug("[delete-folder]: %s", folder_path)
        shutil.rmtree(folder_path)

    def file_delete(self, fname):
        logger.debug("[delete-file]: %s", fname)
        os.remove(fname)

    def file_read(self, fname):
        logger.debug("[read]:%s", fname)
        with open(fname, "r") as f:
            return f.read()

    def file_write(self, text, fname):
        folder_path = os.path.dirname(fname)
        self.folder_create(folder_path)

        logger.debug("[write]:%s", fname)
        with open(fname, "w") as f:
            f.write(text)

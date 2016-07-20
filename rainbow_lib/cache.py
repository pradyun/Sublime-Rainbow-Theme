"""Caches for Rainbow
"""

import os
import abc

from . import core


class Cache(object, metaclass=abc.ABCMeta):
    """Base class for Caches
    """

    @abc.abstractmethod
    def haskey(self, key):
        """Does the key exist in the cache
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, key):
        """Get a value for the key from the cache
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def set(self, key, value):
        """Set a value for the key from the cache
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, key):
        """Delete a value for the key from the cache
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def clear(self):
        """Empty the cache
        """
        raise NotImplementedError()


class NullCache(Cache):
    """A Cache that does not allow any-operation on itself
    """

    def haskey(self, key):
        return False

    def get(self, key):
        raise KeyError("No entries for key: {!r}".format(key))

    def set(self, key, value):
        raise KeyError("No entries for key: {!r}".format(key))

    def delete(self, key):
        raise KeyError("No entries for key: {!r}".format(key))

    def clear(self):
        pass


class FileSystemCache(Cache):
    """A cache for themes and widget-schemes

    NOTE: Could use shelve/persistent-dict.

    Structure:
        cache-dir/
            color1-theme.cache-file
            color1-widget-scheme.cache-file
            color2-theme.cache-file
            color2-widget-scheme.cache-file
    """

    def __init__(self):
        super().__init__()

        self._fsi = core.FileSystemInterfacer()
        self._cache_dir = core.utils.get_path_for("cache")

        core.logger.info("[cache-dir]:{}".format(self._cache_dir))
        self._fsi.folder_create(self._cache_dir)

    def _construct_key_path(self, key):
        return os.path.join(self._cache_dir, key + ".cache-file")

    # ------------------------------------------------------------------------------------
    # API
    # ------------------------------------------------------------------------------------
    def haskey(self, key):
        path = self._construct_key_path(key)
        return self._fsi.exists(path)

    def get(self, key):
        path = self._construct_key_path(key)

        if not self._fsi.exists(path):
            raise KeyError("No entries for key: {!r}".format(key))

        value = self._fsi.file_read(path)

        return value

    def set(self, key, value):
        path = self._construct_key_path(key)
        self._fsi.file_write(value, path)

    def delete(self, key):
        path = self._construct_key_path(key)

        if not self._fsi.exists(path):
            raise KeyError("No entries for key: {!r}".format(key))

        self._fsi.file_delete(path)

    def clear(self):
        self._fsi.folder_delete(self._cache_dir)
        self._fsi.folder_create(self._cache_dir)

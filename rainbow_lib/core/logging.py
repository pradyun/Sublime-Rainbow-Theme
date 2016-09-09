"""Basic logging related things
"""

import logging

from .utils import PACKAGE_NAME

__all__ = ["logger"]

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
logger = logging.getLogger(PACKAGE_NAME)


def setup_logger(preferences):
    if preferences.debug_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

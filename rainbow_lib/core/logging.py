"""Basic logging related things
"""

import logging

from .utils import PACKAGE_NAME, DEBUG_MODE

__all__ = ["logger"]

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
logger = logging.getLogger(PACKAGE_NAME)

if DEBUG_MODE:
    logger.setLevel(logging.DEBUG)

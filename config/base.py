"""
Base settings to build other settings files upon.
"""
import logging
from pathlib import Path

import environs

# (researcher/config/base.py - 3 = researcher/)
ROOT_DIR = Path(__file__).parent.parent

env = environs.Env()

READ_DOT_ENV_FILE = env.bool("READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"), False)


# GOOGLE STORAGRE
# -----------------------------------------------------------------------------
BUCKET_NAME = env("BUCKET_NAME", default="apache-beam-samples")

# LOGGING
# -----------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "level": env("LOGGING_LEVEL", default=logging.WARNING),
        "handlers": ["console"],
    },
    "formatters": {
        "default": {"format": "%(asctime)s %(levelname)s %(name)s | %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
}

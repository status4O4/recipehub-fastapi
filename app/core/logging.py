import logging
import logging.config
from core.config import get_settings

settings = get_settings()


def setup_logging() -> None:
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": ("%(asctime)s | %(levelname)s | %(name)s | %(message)s"),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
        },
        "root": {
            "level": settings.LOG_LEVEL,
            "handlers": ["console"],
        },
        "loggers": {
            # SQLAlchemy (шумно, но полезно в dev)
            "sqlalchemy.engine": {
                "level": "INFO",
                "handlers": ["console"],
                "propagate": False,
            },
            # uvicorn access отдельно
            "uvicorn.access": {
                "level": "INFO",
                "handlers": ["console"],
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(LOGGING_CONFIG)

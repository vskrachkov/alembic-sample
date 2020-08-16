import os
import sys

from alembic.config import Config

sys.path = ["", ".."] + sys.path[1:]

from alembic import command
from sqlalchemy import engine_from_config

from app.db import metadata

config = Config(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "alembic.ini"
    )
)
engine = engine_from_config(config.get_section(config.config_ini_section))


def main():
    metadata.create_all(engine)
    command.stamp(config, "head")


if __name__ == "__main__":
    main()

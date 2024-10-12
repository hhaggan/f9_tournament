from typing import Any

import sqlalchemy
from databases import Database
from heliclockter import datetime_utc

from bracket.config import config


def datetime_decoder(value: str) -> datetime_utc:
    # Handle timezone formatting
    if "+" in value or "-" in value:
        # Split at the timezone marker (+ or -)
        date_part, tz_part = value.rsplit("+", 1) if "+" in value else value.rsplit("-", 1)
        # If the timezone is only hours (e.g. +03), make it +03:00
        if len(tz_part) == 2:
            tz_part = tz_part + ":00"
        value = date_part + "+" + tz_part
    elif "Z" in value:
        # ISO 8601 format with 'Z' (UTC)
        value = value.replace("Z", "+00:00")
    
    # Remove microseconds if present (optional)
    value = value.split(".")[0] if "." in value else value

    # Return the parsed datetime object
    return datetime_utc.fromisoformat(value)


async def asyncpg_init(connection: Any) -> None:
    for timestamp_type in ("timestamp", "timestamptz"):
        await connection.set_type_codec(
            timestamp_type,
            encoder=datetime_utc.isoformat,
            decoder=datetime_decoder,
            schema="pg_catalog",
        )


database = Database(str(config.pg_dsn), init=asyncpg_init)

engine = sqlalchemy.create_engine(str(config.pg_dsn))

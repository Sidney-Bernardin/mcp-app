import os

PG_URL = os.getenv(
    "APP_PG_URL",
    "postgres://postgres:postgres@localhost:5432/postgres?ssl_mode=disable",
)

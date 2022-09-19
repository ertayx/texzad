from peewee import PostgresqlDatabase
from decouple import config

postgres_db = PostgresqlDatabase(
    database=config("DB_NAME"),
    user=config("DB_USER"),
    password=config("DB_PASSWORD"),
    host=config("HOST"),
    port="5432"
)

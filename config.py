from peewee import PostgresqlDatabase

postgres_db = PostgresqlDatabase(
    database="texzad",
    user="ertay",
    password="1",
    host="localhost",
    port="5432"
)

import peewee

from config import postgres_db

from peewee import Model

class BaseModel(Model):
    class Meta:
        database = postgres_db

class Pars(BaseModel):
    date = peewee.CharField(max_length=100)
    images = peewee.CharField(max_length=220, null=True)
    price = peewee.CharField(max_length=50, null=True)

postgres_db.connect()

postgres_db.create_tables([Pars])
from cassandra.cqlengine.models import Model, columns


class User(Model):
    __table_name__ = 'users'

    id = columns.UUID(primary_key=True)
    first_name = columns.Text()
    last_name = columns.Text()
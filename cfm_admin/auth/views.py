from flask_admin.model import BaseModelView
from flask_wtf import Form
from .models import User
from wtforms import StringField, IntegerField


class UserView(BaseModelView):
    model = User
    column_list = (User.id, User.first_name, User.last_name)

    def get_pk_value(self, model):
        return self.model.id

    def scaffold_list_columns(self):
        columns = []

        for p in dir(self.model):
            attr = getattr(self.model, p)
            if isinstance(attr, User.id):
                columns.append(p)

        return columns

    def scaffold_form(self):

        class MyForm(Form):
            id = IntegerField('id')
            first_name = StringField('first_name')
            last_name = StringField('last_name')

        return MyForm

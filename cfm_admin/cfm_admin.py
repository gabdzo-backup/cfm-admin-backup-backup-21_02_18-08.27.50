from flask import Flask
from flask_admin import Admin



from cfm_admin.extensions import db
from cfm_admin.auth.models import User
from cfm_admin.auth.views import UserView
from cfm_admin.database import connect

def create_app(config_object="cfm_admin.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    session = connect()
    register_extensions(app)
    admin = Admin(app, name='Cook For Me Admin', template_mode='bootstrap3')
    admin.add_view(UserView(User, session))
    print(app.config, 'KEKEKEKEKKET')
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    return None

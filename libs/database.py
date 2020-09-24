from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
app.config['FLASK_ADMIN_SWITCH'] = 'cerulean'

admin = Admin(app, name='Cook For Me', template_mode='bootstrap3')

app.run()

cloud_config = {
    'secure_connect_bundle': '/home/gzvoncek/projects/cfm/cfm-admin/libs/secure-connect-cfm.zip'
}

def connect():
    auth_provider = PlainTextAuthProvider(username='cfm_db_admin', password='mamedomawifi')

    cluser = Cluster(cloud=cloud_config, auth_provider=auth_provider)

    session = cluser.connect('cfm')
    rows = session.execute('SELECT name, age, email FROM users')
    for user_row in rows:
        print (user_row.name, user_row.age, user_row.email)
    return session

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': '/home/gzvoncek/projects/cfm/cfm-admin/cfm-admin/secure-connect-cfm.zip'
}


def connect():
    auth_provider = PlainTextAuthProvider(username='cfm_db_admin', password='mamedomawifi')

    cluser = Cluster(cloud=cloud_config, auth_provider=auth_provider)

    session = cluser.connect('cfm')
    rows = session.execute('SELECT name, age, email FROM users')
    for user_row in rows:
        print (user_row.name, user_row.age, user_row.email)
    return session

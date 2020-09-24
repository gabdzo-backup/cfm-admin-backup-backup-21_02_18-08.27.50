from environs import Env

env = Env()
env.read_env()

cloud_config = {
    'secure_connect_bundle':
        '/home/gzvoncek/projects/cfm/cfm-admin/libs/secure-connect-cfm.zip'
}

CASSANDRA_HOSTS = ['https://d5fe239e-b6c5-44e1-b0b1-7082414c2a78-europe-west1.apps.astra.datastax.com']
CASSANDRA_KEYSPACE = "cfm"
# CASSANDRA_SETUP_KWARGS = {'cloud_config': cloud_config}
FLASK_ADMIN_SWATCH = 'cerulean'

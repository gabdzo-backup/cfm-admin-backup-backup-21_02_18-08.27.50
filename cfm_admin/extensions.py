from flask_cqlalchemy import CQLAlchemy

# Here you can override basic Models
from cassandra.cqlengine import connection

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from flask_cqlalchemy import CQLAlchemy


class NewCQLAlchemy(CQLAlchemy):
    auth_provider = PlainTextAuthProvider(username='cfm_db_admin',
                                          password='mamedomawifi')
    # connection.cluster = Cluster(cloud=cloud_config,
    #                              auth_provider=auth_provider)
    cloud = {
        'secure_connect_bundle': '/home/gzvoncek/projects/cfm/cfm-admin/libs/secure-connect-cfm.zip'
    }

    connection.cluster_options = {'cloud': cloud,
                                  'auth_provider': auth_provider}

    def init_app(self, app):
        """Bind the CQLAlchemy object to the app.

        This method set all the config options for the connection to
        the Cassandra cluster and creates a connection at startup.
        """
        self._hosts_ = app.config['CASSANDRA_HOSTS']
        self._keyspace_ = app.config['CASSANDRA_KEYSPACE']
        consistency = app.config.get('CASSANDRA_CONSISTENCY', 1)
        lazy_connect = app.config.get('CASSANDRA_LAZY_CONNECT', False)
        retry_connect = app.config.get('CASSANDRA_RETRY_CONNECT', False)
        setup_kwargs = app.config.get('CASSANDRA_SETUP_KWARGS', {})

        if not self._hosts_ and self._keyspace_:
            raise NoConfig("""No Configuration options defined.
            At least CASSANDRA_HOSTS and CASSANDRA_CONSISTENCY
            must be supplied""")
        connection.setup(self._hosts_,
                         self._keyspace_,
                         consistency=consistency,
                         lazy_connect=lazy_connect,
                         retry_connect=retry_connect,
                         **setup_kwargs)


class NoConfig(Exception):
    """ Raised when CASSANDRA_HOSTS or CASSANDRA_KEYSPACE is not defined"""
    pass


db = NewCQLAlchemy()

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
#
# from flask import Flask
# from flask_admin import Admin
#
# app = Flask(__name__)
# app.config['FLASK_ADMIN_SWITCH'] = 'cerulean'
#
# admin = Admin(app, name='Cook For Me', template_mode='bootstrap3')
#
# app.run()

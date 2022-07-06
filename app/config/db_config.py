import configparser, os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

host = config['postgresql']['host']
user = config['postgresql']['user']
password = config['postgresql']['password']
database = config['postgresql']['database']
port = config['postgresql']['port']
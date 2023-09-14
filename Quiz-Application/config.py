import configparser
import socket

class ConfigClass:

    @staticmethod
    def get_username():
        config = configparser.ConfigParser()
        try:
            config.read('config.ini')
            hostname = socket.gethostname()
            username = config.get(hostname, 'username', fallback='default_username')
            return username
        except (configparser.Error, OSError) as e:
            print(f"Error: {e}")
            return 'default_username' 

import configparser

config = configparser.ConfigParser()
config.read('cal30590config.ini')
print(config['EVENT'].get('TIMEZONE'))

import os,configparser
from icecream import ic

# current_dir = os.path.realpath(__file__).split('\\app_config.py')[0]
current_dir = os.path.realpath(__file__).split('/app_config.py')[0]
config_parser = configparser.ConfigParser()
default_config_file = f"{current_dir}/env.ini"

config_parser.read(default_config_file)

ENV=config_parser.get('APP','ENV')

HOST=config_parser.get(ENV,'HOST')
PORT=int(config_parser.get(ENV,'PORT'))
DEBUGMODE=config_parser.get(ENV,'DEBUGMODE')
SERVICE_URL=str(config_parser.get(ENV,'SERVICE_URL'))
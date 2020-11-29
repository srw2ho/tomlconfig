from functools import reduce
import operator
import os
import toml

class TomlParser:

    def __init__(self, file_name):
        try:
            if os.name == 'nt':
                # program_data_path = os.getenv('ProgramData')
                # if not program_data_path:
                #     program_data_path = 'C:\\ProgramData'
                program_data_path = '../'
                self.file_path = os.path.join(program_data_path, 'appwindowsconfigs', file_name)
            else:
                self.file_path = os.path.join('/etc/appconfigs', file_name)

            self.toml = toml.load(self.file_path)

        except FileNotFoundError as _:
            print(f'Config file not found at {file_name}')
            self.toml = {}
        except toml.decoder.TomlDecodeError as exception:
            print('Invalid config file!')
            print(exception)
            self.toml = {}

    def getFromTOML(self, mapList):
        return reduce(operator.getitem, mapList, self.toml)

    def set_value(self, name, value):
        try:
            reduce(operator.getitem, name.split('.')[:-1], self.toml)[name.split('.')[-1]] = value
        except Exception as e:
            print(e)

    def get(self, name, default_value):
        try:
            if isinstance(name, str):
                value = self.getFromTOML(name.split('.'))
            else:
                value = self.getFromTOML(name)

            # check matching type
            if not isinstance(value, type(default_value)):
                print(f'Type for {name} does not match type {type(default_value)}. Example:')
                suggest_values(name, default_value)
                return default_value

            return value
        except KeyError as _:
            print(f'Key {name} not found in config file. Using default value')
            print("Config should contain:")

            # print suggestion how to configure the config file (in case of error)
            suggest_values(name, default_value)

            return default_value

    def save(self):
        try:
            file = open(self.file_path, "w")
            toml.dump(self.toml, file)
            file.close()
        except Exception as e:
            print(e)

def suggest_values(name, default_value):
    if isinstance(default_value, int) or isinstance(default_value, float) or isinstance(default_value, list):
        print(f'{name} = {default_value}')
    elif isinstance(default_value, str):
        print(f'{name} = "{default_value}"')
    elif isinstance(default_value, bool):
        print(f'{name} = {"true" if default_value else "false"}')

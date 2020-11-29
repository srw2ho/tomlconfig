# srw2ho tomlconfig Configuration Utility Module

### Installation from Repository (online)
```bash
pip install git+https://github.com/srw2ho/tomlutils.git
```

### Configuration

(Linux):

### Usage
```python
from tomlconfig.utils import TomlParser

PROJECT_NAME = 'xxxxxxxx'
toml = Parser(f'{PROJECT_NAME}.toml')

MQTT_NETWORK_NAME = toml.get('mqtt.network_name', 'mh')
MQTT_PORT = toml.get('mqtt.port', 1883)
MQTT_USERNAME = toml.get('mqtt.username', '')

INFLUXDB_FILTER = toml.get('influxdb.filter', [])
```

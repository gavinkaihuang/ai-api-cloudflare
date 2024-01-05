import configparser

section = 'section1'

def get_properties(*keys):
    config = configparser.ConfigParser()
    config.read('config.properties')

    if (len(keys) == 1):
        return config.get(section, keys[0])
    else:
        results = []
        for key in keys:
            results.append(config.get(section, key))
        return results

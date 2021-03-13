import configparser
import os


# init config for first time
# this is not config for whole time running
CONFIG = configparser.ConfigParser()
CONFIG['DEFAULT'] = {
    'BATTERY_LOW': 0.20,
    'MESSAGE': '[battery] renaming!\nCharge your computer\nright now!',
    'ADAPTER': ''
}
LOCATION = {
    'shortly': f"{os.environ['HOME']}/.battery_st.cfg",
    'fully':   f"{os.environ['HOME']}/.config/battery_st/config"
}


def __write_config__(config):
    default_file = 'fully'
    folder_config = os.path.dirname(LOCATION[default_file])
    if os.path.isdir(folder_config) is False:
        os.mkdir(folder_config)

    with open(LOCATION[default_file], 'w') as config_file:
        config.write(config_file)

    return config


def init_config():
    config_file = None
    for key in LOCATION:
        if os.path.isfile(LOCATION[key]):
            print(LOCATION[key])
            config_file = LOCATION[key]
            break

    if config_file:
        _ = configparser.ConfigParser()
        _.read(config_file)
        return _
    else:
        return __write_config__(CONFIG)


def test_config():
    assert CONFIG
    assert __write_config__(CONFIG)
    assert init_config()

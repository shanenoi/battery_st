from glob import glob


class DefaultConfig:
    SOURCE_FILE = glob('/sys/class/power_supply/BAT*/uevent')[0]
    CHARGING_STATUS = 'POWER_SUPPLY_STATUS'
    POWER_FULL = 'POWER_SUPPLY_ENERGY_FULL'
    POWER_NOW = 'POWER_SUPPLY_ENERGY_NOW'

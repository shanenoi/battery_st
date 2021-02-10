import glob
import pprint

class Battery(object):

    def __init__(self, source_file = '/sys/class/power_supply/BAT*/uevent'):
        self.SOURCE_FILE = source_file
        self.info = {}
        self.__load_content()


    def __load_content(self):
        if self.info != {}:
            return

        # find info file
        self.SOURCE_FILE = glob.glob(self.SOURCE_FILE)
        assert len(self.SOURCE_FILE) == 1
        self.SOURCE_FILE = self.SOURCE_FILE[0]

        # load data
        raw_data = [
            line.split('=') for
            line in open(self.SOURCE_FILE).read().split('\n') if line
        ]
        self.info = {
            ele[0]: (int(ele[1]) if ele[1].isdigit() else ele[1])
            for ele in raw_data
        }


    def __str__(self):
        return pprint.pformat(self.info, indent=4)


    def _status(self):
        self.__charging_status = 'POWER_SUPPLY_STATUS'
        return self.info[self.__charging_status]


    def _enery_full(self):
        self.__power_supply_energy_full = 'POWER_SUPPLY_ENERGY_FULL'
        return self.info[self.__power_supply_energy_full]


    def _energy_now(self):
        self.__power_supply_energy_now = 'POWER_SUPPLY_ENERGY_NOW'
        return self.info[self.__power_supply_energy_now]


    def percentage_now(self):
        return self._energy_now() / self._enery_full()

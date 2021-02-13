from pprint import pformat
from . import DefaultConfig


class Battery(object):

    def __init__(self):
        self.SOURCE_FILE = DefaultConfig.SOURCE_FILE
        self.info = {}
        self.__load_content()


    def __load_content(self) -> None:
        if self.info != {}:
            return

        # load data
        raw_data = [
            line.split('=') for
            line in open(self.SOURCE_FILE).read().split('\n') if line
        ]
        self.info = {
            ele[0]: (int(ele[1]) if ele[1].isdigit() else ele[1])
            for ele in raw_data
        }


    def __str__(self) -> str:
        return pformat(self.info, indent=4)


    def _status(self) -> str:
        self.__charging_status = DefaultConfig.CHARGING_STATUS
        return self.info[self.__charging_status]


    def _enery_full(self) -> int:
        self.__power_supply_energy_full = DefaultConfig.POWER_FULL
        return self.info[self.__power_supply_energy_full]


    def _energy_now(self) -> int:
        self.__power_supply_energy_now = DefaultConfig.POWER_NOW
        return self.info[self.__power_supply_energy_now]


    def percentage_now(self) -> float:
        return self._energy_now() / self._enery_full()


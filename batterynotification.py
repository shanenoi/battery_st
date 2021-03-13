from .battery.battery import Battery
from .windows.windows import FastWindows
from .config import init_config

CONFIG = init_config()
BATTERY = Battery()


class Adapter(object):
    config = CONFIG['DEFAULT']
    battery = BATTERY

    def __init__(self):
        pass


    def display(self) -> int:
        FastWindows(self.message).start()
        return 0


    @classmethod
    def _standardized_message(cls: object, message:str) -> str:
        while True:
            current_length = len(message)
            for key in cls.battery.shortcut_access.keys():
                # print(str(cls.battery.shortcut_access[key]))
                message = (message.replace(
                    key,
                    str(cls.battery.shortcut_access[key])[:5]
                )) if key in message else message

            if len(message) == current_length:
                return message


    def run(self) -> int:
        return_code = 0
        print(self.battery.percentage_now)
        print(self.config['BATTERY_LOW'])
        if (
                self.battery.percentage_now <= float(self.config['BATTERY_LOW']) and
                self.battery.charging is False
            ):
            self.message = self._standardized_message(self.config['MESSAGE'])
            return_code = self.display()
        return return_code


def main() -> None:
    pass


if __name__ == '__main__':
    main()

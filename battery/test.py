from .battery import Battery
import inspect
import sys


class TestBattery(Battery):

    prefix_test_cases = 'test_'

    def test_status(self) -> None:
        assert self._status()


    def test_enery_full(self) -> None:
        assert self._enery_full()


    def test_energy_now(self) -> None:
        assert self._energy_now()


    def test_percentage_now(self) -> None:
        assert self._energy_now()


    def test_charging(self) -> None:
        assert self.charging != None


    def test_shortcut_access(self) -> None:
        for key in self.shortcut_access.keys():
            assert self.shortcut_access[key] != None


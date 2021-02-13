from . import FastWindows
from threading import Thread
from time import sleep


def test_create_windows():
    controller = FastWindows('test windows')
    controller.root.after(1000, lambda: controller.close())
    controller.start()

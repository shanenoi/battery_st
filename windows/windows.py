from tkinter import *
from . import DefaultConfig
from threading import Thread


class Window(object):

    def __init__(self):
        self.root = Tk()
        self.root.geometry(DefaultConfig.DEFAULT_GEOMETRY)
        self.root.resizable(width=0, height=0)
        self.root.title(DefaultConfig.DEFAULT_TITLE)
        self.root.configure(background=DefaultConfig.DEFAULT_BACKGROUND)
        self.__set_ups = []


    def set_up(self, function) -> None:
        self.__set_ups.append(function)


    def start(self) -> None:
        for set_up_function in self.__set_ups:
            set_up_function(root = self.root)

        self.root.mainloop()


    def close(self) -> None:
        self.root.destroy()



class Component(object):


    def __init__(self, Model):
        self.model = Model
        self.inner_config = {
            'text': '',
            'bg': DefaultConfig.DEFAULT_BACKGROUND,
            'fg': DefaultConfig.DEFAULT_FOREGROUND,
            'font': DefaultConfig.DEFAULT_FONT,
        }
        self.position = DefaultConfig.DEFAULT_POSITION


    def pack(self, root) -> None:
        component = self.model(root, self.inner_config)
        component.config(self.position)
        component.pack()


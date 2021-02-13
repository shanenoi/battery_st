from tkinter import CENTER


class DefaultConfig:
    DEFAULT_FOREGROUND = 'white'
    DEFAULT_BACKGROUND = 'red'
    DEFAULT_GEOMETRY = '200x100'
    DEFAULT_TITLE = '⚡'
    DEFAULT_FONT = 'none 12 bold'
    DEFAULT_POSITION = {'anchor': CENTER}



def FastWindows(title):
    from tkinter import Label
    window_model = __import__('windows.windows', fromlist=[''])
    windows = window_model.Window()

    @windows.set_up
    def add_title(root):
        label = window_model.Component(Label)
        label.inner_config['text'] = title
        label.pack(root)

    return windows

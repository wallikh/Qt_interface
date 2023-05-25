class check:
    def __init__(self):
        self._ma_variable = None
        self._callbacks = []

    @property
    def ma_variable(self):
        return self._ma_variable

    @ma_variable.setter
    def ma_variable(self, value):
        self._ma_variable = value
        for callback in self._callbacks:
            callback()

    def register_callback(self, callback):
        self._callbacks.append(callback)

def my_callback():
    print("!")

class Register:
    def __init__(self, name: str):
        self.__name__ = name
        self.__value__ = 0

    @property
    def name(self):
        return self.__name__

    @property
    def value(self):
        return self.__value__

    def set_value(self, value):
        self.__value__ = value

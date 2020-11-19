
class LazyContainer:


    """
    Класс-синглтон для хранения инстансов других классов синглтонов
    Например, если есть класс Foo, у которого в конструкторе аргумент bar, то для создания

    Container = LazyContainer()

    Container.set(Foo, bar="something")

    После, для получения

    print(Container[Foo].bar)

    Если нет аргументов, можно просто
    Container(Foo)
    """
    def __init__(self):
        self._c = dict()


    # For functions with no params
    def __setitem__(self, key, value): #value - function
        """
        :param key: Just the index
        :param value: When first assigned - function that returns the desired value
        :return:
        """
        self._c[key] = { "func": value, "params":{} }


    # For functions with params
    def set(self, value, key=None , **kwargs):
        if key == None:
            key = value.__name__
        self._c[key] = { "func": value, "params": kwargs }


    def __getitem__(self, item):
        if isinstance(item, type):
            item = item.__name__
        if callable(self._c[item]["func"]):
            self._c[item]["func"] = self._c[item]["func"](**self._c[item]["params"])
        return self._c[item]["func"]

Container = LazyContainer()

# Для тестов
if __name__ == "__main__":

    class TEST:

        def __init__(self):
            self.bruh = "bruh"

    def testy( st : str ):
        return "This is " + st

    Container.set(testy,"Bruh", st="bruh")
    Container.set(testy,"Tes", st=Container["Bruh"])
    Container.set(TEST)

    print(callable(TEST))

    print(Container["Tes"])

    print(Container["Tes"])

    print(Container[TEST])
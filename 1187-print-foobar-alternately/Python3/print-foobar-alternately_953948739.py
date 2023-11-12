import threading

class FooBar:
    def __init__(self, n):
        self.n = n

        self.__foo_lock = threading.Lock()
        self.__bar_lock = threading.Lock()
        self.__bar_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.__foo_lock.acquire()
            printFoo()
            self.__bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.__bar_lock.acquire()
            printBar()
            self.__foo_lock.release()

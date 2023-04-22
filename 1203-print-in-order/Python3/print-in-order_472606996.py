from threading import Barrier
class Foo:
    def __init__(self):
        self.barrier_one = Barrier(2)
        self.barrier_two = Barrier(2)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.barrier_one.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.barrier_one.wait()
        printSecond()
        self.barrier_two.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.barrier_two.wait()
        printThird()
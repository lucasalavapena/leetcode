from threading import Barrier

class FooBar:
    def __init__(self, n):
        self.n = n
        self.b = Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
        	printFoo()
        	self.b.wait()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            self.b.wait()
            printBar()
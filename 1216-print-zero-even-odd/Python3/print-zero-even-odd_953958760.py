from threading import Semaphore


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.curr = 0 
        self.zero_gate = Semaphore(1)
        self.odd_gate = Semaphore(0)
        self.even_gate = Semaphore(0)

        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.zero_gate.acquire()
            printNumber(0)
            self.curr += 1
            if self.curr % 2:
                self.odd_gate.release()
            else:
                self.even_gate.release()


        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n//2):           
            self.even_gate.acquire()
            printNumber(self.curr)
            self.zero_gate.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1)//2):
            self.odd_gate.acquire()
            printNumber(self.curr)
            self.zero_gate.release()
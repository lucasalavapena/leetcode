from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.b = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.sem_h:
            self.b.wait()
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            self.b.wait()
            releaseOxygen()
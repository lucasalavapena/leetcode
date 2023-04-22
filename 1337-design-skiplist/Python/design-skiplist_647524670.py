from sortedcontainers import SortedList

class Skiplist(object):

    def __init__(self):
        self.l = SortedList()

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.l

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.l.add(num)
        

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num in self.l:
            self.l.remove(num)
            return True
        return False
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
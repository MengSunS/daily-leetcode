class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = collections.defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        #这里的坑是有没有都得insert,所以不能判断有就return False
        self.dict[val].add(len(self.list))
        self.list.append(val)
        return len(self.dict[val]) == 1 #之前没有现在是1，true, else: false
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # 这里的坑是别del self.dict[val],不然要写两次，后面的self.dict[slef.list[-1]]还要写一次，因为有add, remove-> can be set()
        if not self.dict[val]: return False
        idx = self.dict[val].pop()
        self.list[idx] = self.list[-1]
        self.dict[self.list[-1]].add(idx)
        self.dict[self.list[-1]].remove(len(self.list) - 1)
        self.list.pop()
        return True

        
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        # choice函数，random library 
        return choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class MyCalendarThree:

    def __init__(self):
        self.time = defaultdict(int)
        

    def book(self, start: int, end: int) -> int:
        self.time[start] += 1
        self.time[end] -= 1
        
        res, count= 0, 0
        for x in sorted(self.time):
            count += self.time[x]
            res= max(res, count)
            
        return res
        

        
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

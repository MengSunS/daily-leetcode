class SnapshotArray:

    def __init__(self, length: int):
        self.l = [0] * length
        self.snapshots = {}
        self.id = -1
        self.d = {}
        

    def set(self, index: int, val: int) -> None:
        self.l[index] = val
        self.d[index] = val
        

    def snap(self) -> int:
        self.id += 1
        d_copy = dict(self.d)
        self.snapshots[self.id]= (d_copy)
        return self.id
        
        

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.snapshots[snap_id]:
            return 0
        else:
            return self.snapshots[snap_id][index]
       
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# [6 0 0]
# 0: [5 0 0]  
    

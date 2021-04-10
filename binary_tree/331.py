class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        prev = ','
        for p in preorder:
            if p != ',' and prev == ',':
                slots -= 1
                if slots < 0:
                    return False

                if p != '#':
                    slots += 2
            prev = p
        return slots == 0
            
        

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            area += (y2 - y1) * (x2 - x1)
            for c in list(itertools.product([x1, x2], [y1, y2])):
                if c in corners:
                    corners.remove(c)
                else:
                    corners.add(c)
        if len(corners) != 4:
            return False
        corners = sorted(corners)
        return area == (corners[-1][1] - corners[0][1]) * (corners[-1][0] - corners[0][0])
        
                    
            
        

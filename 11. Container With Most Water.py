class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxarea = min(height[p1], height[p2]) * (p2-p1)
        while p2 > p1:
            if height[p1] <= height[p2]:
                p1 = p1 + 1
            else:
                p2 = p2 - 1
            maxarea = max(maxarea, min(height[p1], height[p2]) * (p2-p1))
        return maxarea
    
    
### this is a two pointer method: go from the largest width, each time reduce width by 1 
### because here the smaller number in the pair determine the cap area of the container, 
### each time when we reduce the width by 1, we move the pointer from the smaller number to the next one in order to look for larger number(larger area)

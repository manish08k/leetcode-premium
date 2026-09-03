# Definition for a street.
# class Street:
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
class Solution:
    def tryMoveToOpen(self, street: Optional['Street'], k: int, consider_current: bool) -> int:
        if street.isDoorOpen() and consider_current:
            return 0
        r = 1
        street.moveRight()
        while not street.isDoorOpen() and r <= k:
            street.moveRight()
            r += 1
        return r
    
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        r = 0
        while True:
           self.tryMoveToOpen(street, k, True)
           d = self.tryMoveToOpen(street, k, False)
           if d > k:
               return r
           r = d
           street.closeDoor()
        return -1
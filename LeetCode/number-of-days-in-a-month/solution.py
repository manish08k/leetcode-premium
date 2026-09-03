class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        look='135781012'
        if month==2:
            return 29 if ((year%4==0 and year%100!=0) or (year%400==0)) else 28
        elif str(month) in look:
            return 31
        else:
            return 30
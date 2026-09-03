"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        time = defaultdict(int)
        for employee in schedule:
            for interval in employee:
                time[interval.start] += 1
                time[interval.end] -= 1
        result = []
        count = 0
        start = None
        for index, value in sorted(time.items()):
            count += value
            if count == 0:
                start = index
            elif start != None:
                result.append(Interval(start, index))
                start = None
        return result
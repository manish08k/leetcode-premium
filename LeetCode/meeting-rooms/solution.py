class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals = sorted(intervals)

        if len(intervals) == 0:
            return True

        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:

            if prev_end > start:
                return False

            prev_end, prev_start = end, start

        return True
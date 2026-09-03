class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        max_students = 0
        freq_dict = {}
        for si, bi in students:
            if bi not in freq_dict:
                freq_dict[bi] = set([si])
            else:
                freq_dict[bi].add(si)
            max_students = max(
                max_students,
                len(freq_dict[bi])
            )
        return max_students
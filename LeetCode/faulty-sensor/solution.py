class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        l, r = 0, 0
        while l < n - 1 and r < n - 1:
            if sensor1[l] != sensor2[r]:
                if (
                    sensor1[l:n - 1] == sensor2[r + 1:]
                    and not (sensor2[r:n - 1] == sensor1[l + 1:])
                ):
                    return 1
                elif (
                    sensor2[r:n - 1] == sensor1[l + 1:]
                    and not (sensor1[l:n - 1] == sensor2[r + 1:])
                ):
                    return 2
            l += 1
            r += 1
        return -1
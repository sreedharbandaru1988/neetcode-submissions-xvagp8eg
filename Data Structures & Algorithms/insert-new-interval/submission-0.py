class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = output[-1]
            if last[1] >= curr[0]:
                last[1] = max(last[1], curr[1])
            else:
                output.append(curr)
        return output
        
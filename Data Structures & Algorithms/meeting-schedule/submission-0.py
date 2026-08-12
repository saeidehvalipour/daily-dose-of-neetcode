from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Edge case
        if not intervals:
            return True

        # 1️⃣ sort by start time
        intervals.sort(key=lambda x: x.start)

        # 2️⃣ check overlap
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True

from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for x in nums:
            self._push(x)

    def _push(self, val: int) -> None:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        self._push(val)
        return self.heap[0]

        

# from bisect import bisect_left
#
#
# class RecentCounter:
#
#     def __init__(self):
#         self.calls = []
#
#
#     def ping(self, t: int) -> int:
#         self.calls.append(t)
#         return len(self.calls) - bisect_left(self.calls, t - 3000)


from collections import deque


class RecentCounter:

    def __init__(self):
        self.calls = deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.popleft()

        return len(self.calls)

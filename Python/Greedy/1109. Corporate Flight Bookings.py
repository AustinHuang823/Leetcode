from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for _ in range(n+1)]
        for operations in bookings:
            res[operations[0]-1] += operations[2]
            res[operations[1]] -= operations[2]
        tmp = 0
        for i in range(len(res)):
            tmp += res[i]
            res[i] = tmp
        return res[:n]

if __name__ == '__main__':
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    sol = Solution()
    print(sol.corpFlightBookings(bookings,n))
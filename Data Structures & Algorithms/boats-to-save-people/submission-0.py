class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        L = 0
        R = len(people)-1
        while L <= R:
            count += 1
            if people[L] + people[R] <= limit:
                L += 1
            R -= 1
        return count

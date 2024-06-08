class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = []
        result = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            distances.append([distance, x, y])
        distances.sort(key = lambda x:(-x[0]))
        while k > 0:
            distance, x, y = distances.pop()
            result.append([x, y])
            k -= 1
        return result
        
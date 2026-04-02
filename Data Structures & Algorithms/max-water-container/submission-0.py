class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = float("-inf")
        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         height = min(heights[i],heights[j])
        #         width = j - i
        #         area = max(area, height * width)
        # return area

        L = 0
        R = len(heights) - 1
        area = float("-inf")
        while L < R:
            height = min(heights[L],heights[R])
            width = R - L
            area = max(area, height * width)
            if heights[L] < heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return area



        
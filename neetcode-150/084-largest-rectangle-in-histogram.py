class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # for the case of continuous increasingg stack to executed at the end of for loop
        st = [-1] # Since we add 0 at the end any safeguard calculation of height[-1] is done on 0 height. Also w = i - st[-1]- 1 When we dont have any more bars ater st.pop()
        area = 0
        for i in range(len(heights)):
            while st and heights[i] < heights[st[-1]]:
                j = st.pop()
                area = max(area, (i-st[-1]-1)*heights[j])
            st.append(i)
        return area
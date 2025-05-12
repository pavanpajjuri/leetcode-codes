class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n = len(position)
        # time = []
        # for d,v in zip(position,speed):
        #     time.append((target-d)/v)

        # d_t = sorted(zip(position,time), reverse = True)
        # _ , t = zip(*d_t)
        # t = list(t)

        # ans = 1
        # for i in range(1,n):
        #     if t[i] > t[i-1]:
        #         ans += 1
        #     elif t[i] < t[i-1]:
        #         t[i] = t[i-1]
        
        # return ans

        d_v = sorted(zip(position,speed), reverse = True)
        st = []
        for d,v in d_v:
            t = (target-d)/v
            if not st or t > st[-1]:
                st.append(t)
        
        return len(st)
        
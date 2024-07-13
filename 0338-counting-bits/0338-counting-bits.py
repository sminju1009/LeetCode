class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            cnt = 0 # 1이 들어간 횟수
            if i==0:
                answer.append(0)
            elif i==1:
                answer.append(1)
            else:
                share, mod = i//2, i%2
                if mod==1:
                    cnt += 1
                while share>0:
                    share, mod = share//2, share%2
                    if mod==1:
                        cnt += 1
                answer.append(cnt)
        return answer
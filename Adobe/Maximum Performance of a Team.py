import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        eng = []
        for i in range(n):
            eng.append((speed[i],efficiency[i]))
            
                
        eng.sort(key=lambda x:-x[1])
        q = []
        speed = 0
        result = 0
        
        for i,(s,e) in enumerate(eng):
            
            if i < k:
                speed += s
                heapq.heappush(q,s)
            elif s > q[0] :
                speed += s - heapq.heappushpop(q,s)
            else:
                continue
                
            result = max(result, speed * e)
            
        return result % 1000000007

import math
class Solution:
    def countFactors (self, N):
        count=0
        n=int(math.sqrt(N))
        for i in range(1,n+1):
            if N%i==0:
                count+=1
                if i!=N//i:
                    count+=1
        return count




#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.countFactors(N))
        print("~")
# } Driver Code Ends

class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        count = 0
        for num in arr:
            if num <= k:
                count += 1
        
        bad = 0
        for i in range(count):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        for i in range(count, n):
            if arr[i - count] > k:
                bad -= 1
            if arr[i] > k:
                bad += 1
            ans = min(ans, bad)
        
        return ans


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter value of k: "))
    
    sol = Solution()
    print("Minimum swaps required:", sol.minSwap(arr, k))

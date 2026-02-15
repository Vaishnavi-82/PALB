class Solution:
    def threeWayPartition(self, arr, a, b):
        n = len(arr)
        start = 0
        end = n - 1
        i = 0
        
        while i <= end:
            if arr[i] < a:
                arr[i], arr[start] = arr[start], arr[i]
                start += 1
                i += 1
            elif arr[i] > b:
                arr[i], arr[end] = arr[end], arr[i]
                end -= 1
            else:
                i += 1
        
        return arr


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    
    sol = Solution()
    result = sol.threeWayPartition(arr, a, b)
    
    print("Partitioned array:", result)

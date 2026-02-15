import bisect

class Solution:
    def median(self, mat):
        r = len(mat)
        c = len(mat[0])
        
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        
        desired = (r * c) // 2
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            for row in mat:
                count += bisect.bisect_right(row, mid)
            
            if count <= desired:
                low = mid + 1
            else:
                high = mid
        
        return low


if __name__ == "__main__":
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    
    mat = []
    print("Enter matrix row by row:")
    for _ in range(r):
        mat.append(list(map(int, input().split())))
    
    sol = Solution()
    print(sol.median(mat))

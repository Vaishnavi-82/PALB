class Solution:
    def spirallyTraverse(self, mat):
        result = []
        if not mat:
            return result
        
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1
        
        while top <= bottom and left <= right:
            
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        
        return result


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    mat = []
    for _ in range(rows):
        mat.append(list(map(int, input().split())))
    
    sol = Solution()
    print("Spiral order:", sol.spirallyTraverse(mat))

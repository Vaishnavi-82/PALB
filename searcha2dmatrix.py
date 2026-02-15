class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // cols][mid % cols]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    target = 3

    obj = Solution()
    result = obj.searchMatrix(matrix, target)

    print(result)

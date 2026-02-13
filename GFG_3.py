class Solution:
    def findUnion(self, a, b):
        return list(set(a) | set(b))


if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    obj = Solution()
    result = obj.findUnion(a, b)

    print(result)

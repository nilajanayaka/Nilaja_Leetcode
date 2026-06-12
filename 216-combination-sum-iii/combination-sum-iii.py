class Solution:
    def combinationSum3(self, k : int, n: int):
        
        result = []

        def backtrack(start, path, total):

            # Found k numbers
            if len(path) == k:

                if total == n:
                    result.append(path[:])

                return

            for num in range(start,10):

                path.append(num)

                backtrack(num + 1,
                          path,
                          total + num)

                path.pop()

        backtrack(1, [], 0)

        return result
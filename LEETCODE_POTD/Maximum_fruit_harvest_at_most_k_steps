class Solution:
    def lower_bound(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def upper_bound(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        prefix_sum = [0] * n
        indices = [0] * n

        for i in range(n):
            indices[i] = fruits[i][0]
            prefix_sum[i] = fruits[i][1] + (prefix_sum[i - 1] if i > 0 else 0)

        max_fruits = 0

        for d in range(k // 2 + 1):
            remain = k - 2 * d

            # Case 1: move left d steps, then right (k - 2d)
            i = startPos - d
            j = startPos + remain
            left = self.lower_bound(indices, i)
            right = self.upper_bound(indices, j) - 1

            if left <= right:
                total = prefix_sum[right] - (prefix_sum[left - 1] if left > 0 else 0)
                max_fruits = max(max_fruits, total)

            # Case 2: move right d steps, then left (k - 2d)
            i = startPos - remain
            j = startPos + d
            left = self.lower_bound(indices, i)
            right = self.upper_bound(indices, j) - 1

            if left <= right:
                total = prefix_sum[right] - (prefix_sum[left - 1] if left > 0 else 0)
                max_fruits = max(max_fruits, total)

        return max_fruits

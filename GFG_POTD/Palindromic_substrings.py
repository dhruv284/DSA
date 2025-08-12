class Solution:
    def countPali(self, i, j, s):
        count = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
        return count

    def countPS(self, s):
        n = len(s)
        result = 0
        for i in range(n):
            result += self.countPali(i, i + 1, s)  # even length palindromes
            result += self.countPali(i, i, s)      # odd length palindromes
        return result - n  # subtract single-character palindromes

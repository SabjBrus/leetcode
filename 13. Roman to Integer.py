# Roman numerals are represented by seven different symbols:
# I, V, X, L, C, D and M.

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans


n = Solution()
print(n.romanToInt("LVIII"))
print(n.romanToInt("XI"))
print(n.romanToInt("IX"))

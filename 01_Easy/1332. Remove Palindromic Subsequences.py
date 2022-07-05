class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        # let l be the front part and r be the last part of the string
        l,r = 0, len(s)-1
        
        # only three cases, one is 0, another is the string is already a palindrom so return 1, otherwise aaaaa bb are both palindroms, so return 2
        while l<r:
            if s[l] != s[r]: return 2
            r -= 1
            l += 1
        return 1

if __name__ == "__main__":
    sol = Solution()
    test_1 = ("ababa", 1) #(input, expected result)
    test_2 = ("abb", 2)
    tests = (test_1, test_2)
    for idx, (test_case, expected_result) in enumerate(tests):
        result = sol.removePalindromeSub(test_case)
        print(result)
        if result == expected_result:
            print(f"test {idx + 1} passed")
        else:
            print(f"test {idx + 1} failed")
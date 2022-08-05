
class Solution:
    def decodeString(self, s: str) -> str:
        number, stack = 0, ['']
        for character in s:
            if character.isdigit():
                number = number * 10 + int(character)
            elif character == "[":
                stack.append(number)
                number = 0
                stack.append('')
            elif character == "]":
                pattern = stack.pop()
                repeat = stack.pop()
                prefix = stack.pop()
                stack.append(prefix + pattern * repeat)
            else:
                stack[-1] += character

        return ''.join(stack)        
        
if __name__ == '__main__':
    sol = Solution()
    s = "3[a]2[bc]"
    print(sol.decodeString(s))
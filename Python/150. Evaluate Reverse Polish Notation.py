import collections
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        q = collections.deque([])
        operators = set(['+', '-', '*', '/'])

        for op in tokens:
            if op not in operators:
                q.append(int(op))
            else:
                n2 = q.pop()
                n1 = q.pop()
                if op == '+':
                    q.append(n1+n2)
                elif op == '-':
                    q.append(n1-n2)
                elif op == '*':
                    q.append(n1*n2)
                elif op == '/':
                    n = int(n1/n2)
                    if n < 0 and n1 % n2: n += 1
                    q.append(n)

        return q.pop()

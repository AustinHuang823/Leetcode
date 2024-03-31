class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        res = []
        for i in range(len(p)):
            if not p[i] or p[i] == '.': 
                continue
            if res and p[i] == '..':
                res.pop()
                continue
            elif not res and p[i] == '..':
                continue

            res.append(p[i])
        s_res = ""
        for r in res:
            s_res += "/"+r
        if not s_res:
            return "/"
        return s_res

from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()

        for x in range(len(searchWord)):
            if len(products) < x:
                products.append("")
        
        l, r = 0, len(products) - 1
        for i,c in enumerate(searchWord):
            # c = searchWord[i]   #if the "for" line is range(len(searchWord))

            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            
            res.append([])
            remain = r - l + 1
            for j in range(min(3,remain)):
                res[-1].append(products[l+j])
        return res

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         n = len(products)
#         products.sort()  # Sort by increasing lexicographically order of products
#         ans = []
#         startIdx, endIdx = 0, n - 1
#         for i, c in enumerate(searchWord):
#             while startIdx <= endIdx and (i >= len(products[startIdx]) or products[startIdx][i] != c):
#                 startIdx += 1
#             while startIdx <= endIdx and (i >= len(products[endIdx]) or products[endIdx][i] != c):
#                 endIdx -= 1

#             if startIdx <= endIdx:
#                 ans.append(products[startIdx:min(startIdx+3, endIdx+1)])
#             else:
#                 ans.append([])
#         return ans

if __name__ == '__main__':
    products = ["havana"]
    searchWord = "havana"
    sol = Solution()
    print(sol.suggestedProducts(products, searchWord))
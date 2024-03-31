class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_lvl = 0
        current_lvl_list = [poured]
        next_lvl_list = []
        while current_lvl < query_row:
            next_lvl_list = [0.] * (current_lvl+2)
            for i in range(current_lvl+1):
                next_pour = (current_lvl_list[i]-1)/2
                if next_pour < 0:
                    next_pour = 0
                next_lvl_list[i] += next_pour
                next_lvl_list[i+1] += next_pour
            current_lvl_list = next_lvl_list
            current_lvl += 1

        return current_lvl_list[query_glass] if current_lvl_list[query_glass] < 1 else 1

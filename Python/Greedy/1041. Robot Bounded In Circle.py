import collections
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]

        def go(pos, idx_direction, behavior):
            if behavior == 'G':
                pos = [pos[0]+direction[idx_direction][0],pos[1]+direction[idx_direction][1]]
            elif behavior == 'L':
                idx_direction -= 1
                if idx_direction < 0:
                    idx_direction = 3
            elif behavior == 'R':
                idx_direction += 1
                if idx_direction > 3:
                    idx_direction = 0
            return pos, idx_direction
        
        instructions = collections.deque(4*instructions)
        pos, idx_direction = [0,0], 0
        while instructions:
            pos, idx_direction = go(pos, idx_direction, instructions.popleft())

        return True if pos == [0,0] else False





if __name__ == '__main__':
    instructions = "GGLLGGG"
    sol = Solution()
    print(sol.isRobotBounded(instructions))
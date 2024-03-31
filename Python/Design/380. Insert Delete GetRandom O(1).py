class RandomizedSet:

    def __init__(self):
        self.elements_map = {}
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.elements_map:
            return False
        self.elements_map[val] = len(self.elements)
        self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.elements_map:
            return False
        idx_to_remove = self.elements_map[val]
        last_num = self.elements[-1]

        self.elements_map[last_num] = idx_to_remove
        self.elements[idx_to_remove] = last_num
        self.elements = self.elements[:-1]
        self.elements_map.pop(val)
        return True

    def getRandom(self) -> int:
        return self.elements[int(random.random()*9999999 % len(self.elements))]


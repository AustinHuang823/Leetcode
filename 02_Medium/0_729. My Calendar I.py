import bisect


class BSTNode:
    def __init__(self, start: int = -1, end: int = -1):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar: #Passed solution #credit by Rocky-Zhenxiang-Fang
    """
    Idea:
        Since we want the event to be sorted and able to lookup, we can create a BST for this
    """

    def __init__(self):
        self.root = BSTNode()

    def book(self, start: int, end: int) -> bool:
        new_event = BSTNode(start, end)
        return self._insert(self.root, new_event)

    def _insert(self, parent: BSTNode, node: BSTNode) -> bool:
        """
        Insert a node to self.root
        :param node: new node to be inserted
        :param parent: current node
        :return: if not double booked, add this leaf and return True, otherwise, return False
        """
        if parent.start <= node.start < parent.end or node.start <= parent.start < node.end:
            return False
        else:
            if parent.start > node.start:
                if not parent.right:
                    parent.right = node
                    return True
                else:
                    return self._insert(parent.right, node)
            else:
                if not parent.left:
                    parent.left = node
                    return True
                else:
                    return self._insert(parent.left, node)

class MyCalendar2: #my solution without sef __init__(self) (optimize halfdone

    # def __init__(self):
    memory_list = []
    l, r = 0, len(memory_list) - 1
    def book(self, start: int, end: int) -> bool:
        pivot = len(self.memory_list) // 2
        while self.l < self.r:
            if self.memory_list[pivot][0] <= start: self.l = pivot
            else: self.r = pivot
        
        for s, e in self.memory_list[pivot-1 : pivot + 1]:
            if  s <= start < e or s < end <= e:
                return False
        self.memory_list.insert(pivot-1, [start, end])
        print(pivot, self.memory_list)
        return True
        

if __name__ == '__main__':
    calender = MyCalendar()
    passed_calender = MyCalendar2()
    input_ex = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
    output1 = []
    output_passed = [] 
    
    for i1, i2 in input_ex:
        output1.append(calender.book(i1, i2))
        output_passed.append(passed_calender.book(i1, i2))
    print(output1,output_passed)
    if output1 == output_passed : print("my solution is correct")
    else: print("the solution is wrong")
        

        

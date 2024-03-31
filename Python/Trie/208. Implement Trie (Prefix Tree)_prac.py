class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.EndOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word) -> None:
        ptr = self.root

        for w in word:
            if w not in ptr.children:
                ptr.children[w] = TrieNode()
            ptr = ptr.children[w]
        ptr.EndOfWord = True

    def search(self, word) -> bool:
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        if ptr.EndOfWord == True:
            return True
        return False
    
    def startsWith(self, word) -> bool:
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        return True
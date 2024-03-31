class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.EndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root

        for w in word:
            if w not in ptr.children:
                ptr.children[w] = TrieNode()
            ptr = ptr.children[w]
        ptr.EndOfWord = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        if ptr.EndOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for w in prefix:
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.end=True

    def search(self, word: str) -> bool:
        cur=self.root
        def recursive(cur, i):
            if i==len(word):
                if cur.end:
                    return True
                return False
            if word[i]=='.':
                if not cur.children:
                    return False
                for child in cur.children.values():
                    cur=child
                    if recursive(cur, i+1):
                        return True
                return False
            else:
                if word[i] not in cur.children:
                    return False
                cur=cur.children[word[i]]
                return recursive(cur, i+1)
        return recursive(cur,0)
        

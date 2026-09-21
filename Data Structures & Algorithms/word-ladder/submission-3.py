class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n=len(wordList[0])
        if n==0:
            return 0
        hash=defaultdict(list)
        
        for word in wordList:
            diff=0
            for i in range(n):
                if word[i]!=beginWord[i]:
                    diff+=1
                    if diff>1:
                        break
            if diff==1:
                hash[beginWord].append(word)
                
        j=0
        while j<len(wordList):
            cur=wordList[j]
            for word in wordList:
                diff=0
                for i in range(n):
                    if word[i]!=cur[i]:
                        diff+=1
                        if diff>1:
                            break
                if diff==1:
                    hash[cur].append(word)
            j+=1
        
        res=0
        q=collections.deque([beginWord])
        s=set()
        s.add(beginWord)
        while q:
            res+=1
            for k in range(len(q)):
                cur=q.popleft()
                for w in hash[cur]:
                    if w==endWord:
                        return res+1
                    if w not in s:
                        s.add(w)
                        q.append(w)

        return 0  

        
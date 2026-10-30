class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        bas1=bas2=0
        type1=type2=-1
        l=0
        maxN=0
        for r in range(len(fruits)):
            if type1==fruits[r]:
                bas1+=1
            elif type2==fruits[r]:
                bas2+=1
            elif type1==-1:
                type1=fruits[r]
                bas1+=1
            elif type2==-1:
                type2=fruits[r]
                bas2+=1
            else:
                while (l<r):
                    if fruits[l]==type1:
                        bas1-=1
                        l+=1
                        if bas1==0:
                            type1=fruits[r]
                            bas1+=1
                            break
                    else:
                        bas2-=1
                        l+=1
                        if bas2==0:
                            type2=fruits[r]
                            bas2+=1
                            break
            maxN=max(maxN, bas1+bas2)

        return maxN

        
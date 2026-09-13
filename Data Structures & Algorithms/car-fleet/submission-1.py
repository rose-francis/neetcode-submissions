class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            position[i]=[position[i],speed[i]]
        position.sort(reverse=True)

        stack=[]
        for el in position:
            time=(target-el[0])/el[1]
            if stack!=[]:
                if stack[-1]<time:
                    stack.append(time)
            else:
                stack.append(time)
        
        return len(stack)

        
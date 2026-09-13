class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        
        heap=[]
        for num in count:
            n=len(heap)
            if len(heap)<k:
                heap.append((count[num],num))
                p=(n-1)//2
                if heap[p][0]>heap[n][0]:
                    self.heapify_up(heap)
            elif len(heap)==k:
                if heap[0][0]<count[num]:
                    heap[0]=(count[num],num)
                    self.heapify_down(heap)
        
        res=[]
        for i,n in enumerate(heap): 
            res.append(heap[i][1])
        return res



    def heapify_up(self,heap):
        i=len(heap)-1
        p=(i-1)//2
        while i>0:
            if heap[i][0]<heap[p][0]:
                temp=heap[i]
                heap[i]=heap[p]
                heap[p]=temp
                i=p
                p=(i-1)//2
            else:
                break

    def heapify_down(self,heap):
        i=0
        l=1
        r=2
        while l<len(heap) or r<len(heap):
            if l<len(heap) and r<len(heap):
                if heap[l][0]<heap[r][0]:
                    min=l
                else:
                    min=r
            elif l<len(heap) and r>=len(heap):
                min=l
            if heap[i][0]>heap[min][0]:
                temp=heap[i]
                heap[i]=heap[min]
                heap[min]=temp
                i=min
                l=2*i+1
                r=2*i+2
            else:
                break
    






        




            

            

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        
        heap=[]
        for num in count:
            if len(heap)<k:
                heap.append((count[num],num))
                self.heapify_up(heap)
            else:
                if heap[0][0]<count[num]:
                    heap[0]=(count[num],num)
                    self.heapify_down(heap)
        
        res=[]
        for i,n in enumerate(heap): 
            res.append(heap[i][1])
        return res



    def heapify_up(self,heap):
        i=len(heap)-1
        while i>0:
            p=(i-1)//2
            if heap[i][0]<heap[p][0]:
                heap[p],heap[i]=heap[i],heap[p]
                i=p
            else:
                break

    def heapify_down(self,heap):
        i=0
        n=len(heap)
        while True:
            l=2*i+1
            r=2*i+2
            min=i
            if l<n and heap[l][0]<heap[min][0]:
                min=l
            if r<n and heap[r][0]<heap[min][0]:
                min=r
            if min!=i:
                heap[min],heap[i]=heap[i],heap[min]
                i=min
            else:
                break
    






        




            

            

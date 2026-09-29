class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and k==1:
            return nums[0]

        heap=[0]*k
        l=1
        heap[0]=nums[0]

        def heapify_down(i):
            while True:
                l = 2*i + 1
                r = 2*i + 2

                if l >= k:
                    break

            
                smallest = l
                if r < k and heap[r] < heap[l]:
                    smallest = r

                
                if heap[i] <= heap[smallest]:
                    break

                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest

        def heapify_up(i):
            p=(i-1)//2
            while p>=0:
                if heap[p]>heap[i]:
                    heap[p],heap[i]=heap[i],heap[p]
                else:
                    break
                i=p
                p=(i-1)//2

        for i in range(1,len(nums)):
            if i>k-1:
                if nums[i]>heap[0]:
                    heap[0]=nums[i]
                    heapify_down(0)
                else:
                    continue
            if i<=k-1:
                heap[i]=nums[i]
                heapify_up(i)
    
        return heap[0]
        

            
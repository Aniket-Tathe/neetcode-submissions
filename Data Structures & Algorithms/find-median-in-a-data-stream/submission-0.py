class MedianFinder:

    def __init__(self):
        self.median = []

    def addNum(self, num: int) -> None:
        # if num:
        self.median.append(num)
        

    def findMedian(self) -> float:
        self.median.sort()
        n=len(self.median)
        if n % 2 !=0:
            # return sum(self.median)/len(self.median)
            return self.median[n//2]
        else:
            return (self.median[(n // 2)-1] + self.median[n//2])/2
        
class Difference:
        
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        maxDiff = 0
        self.maximumDifference = 0
        for i in range(len(a)):
            for j in range (len(a)):
                diff = abs (a[i] - a [j])
                
                if diff > maxDiff :
                    maxDiff = diff
                    self.maximumDifference = maxDiff
            
    def Difference(self,a):
        print (a)
        
    
        
    


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
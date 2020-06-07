import sys

class Solution:
    # Write your code here
    stack = []
    queue = []
    x = 0
    y = 0
    z = 0 
    def pushCharacter(self,char) :
        self.stack.append(char)
        self.x = self.x + 1
        
    def popCharacter(self) :
        self.x = self.x - 1
        #print (self.x , ":" , self.stack[self.x])
        return (self.stack[self.x])
    
    def enqueueCharacter(self,char):
        self.queue.append(char) 
        self.y = self.y + 1
        
    def dequeueCharacter(self) :
        #print (self.queue , "#" , self.z , "#" , self.queue[self.z])
        if self.z == 0 :
            self.z = self.z + 1
            return (self.queue[0])
        else:
            self.z = self.z + 1
            return (self.queue[self.z - 1])


            
        
    

# read the string s
#s=input()
s = 'racecar'
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
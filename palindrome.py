class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x1=x
        s=0
        while x!=0:
            r=x%10
            s=s*10+r
            x=x//10
        if x1==s:
            return True
        else:
            return False
#this code is slow as fuck
#fast as fuck code:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
from typing import List

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        l_num = instructions.count('L')
        r_num = instructions.count('R')
        
        if (l_num-r_num)%4 ==0:
            return False
        else:
            return True

if __name__ == '__main__':
    ssss = Solution()
    names = "GLRLLGLL"
    print(ssss.isRobotBounded(names))
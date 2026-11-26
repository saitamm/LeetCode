class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        Even = 0
        Odd = 0
        for i in range(len(piles)):
            if i % 2 == 0 :
                Even += piles[i]
            else :
                Odd += piles[i]
        print("Even  = ", Even )
        print("Odd = ",  Odd)
        return True
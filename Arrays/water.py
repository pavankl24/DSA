class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total_drunk = numBottles
        empty_bottles = numBottles
        
        while empty_bottles >= numExchange:
            new_full = empty_bottles // numExchange
            rem_empty = empty_bottles % numExchange
            
            total_drunk += new_full
            empty_bottles = new_full + rem_empty
            
        return total_drunk

class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        current_val = 1
        
        for k in range(1, rowIndex + 1):
            current_val = current_val * (rowIndex - k + 1) // k
            row.append(current_val)
            
        return row

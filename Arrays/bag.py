class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        low = 0
        high = len(tokens) - 1
        score = 0
        max_score = 0
        
        while low <= high:
            if power >= tokens[low]:
                power -= tokens[low]
                score += 1
                low += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[high]
                score -= 1
                high -= 1
            else:
                break
                
        return max_score

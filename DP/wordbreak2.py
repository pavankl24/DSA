class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}
        
        def dfs(sub_s):
            if sub_s in memo:
                return memo[sub_s]
            if not sub_s:
                return [""]
                
            res = []
            for i in range(1, len(sub_s) + 1):
                prefix = sub_s[:i]
                if prefix in word_set:
                    sub_sentences = dfs(sub_s[i:])
                    for sub in sub_sentences:
                        if sub:
                            res.append(prefix + " " + sub)
                        else:
                            res.append(prefix)
                            
            memo[sub_s] = res
            return res
            
        return dfs(s)

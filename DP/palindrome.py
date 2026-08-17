class Solution:
    def partition(self, s):
        result = []
        
        def is_palindrome(sub_str):
            return sub_str == sub_str[::-1]
            
        def backtrack(start, path):
            if start == len(s):
                result.append(list(path))
                return
                
            for end in range(start + 1, len(s) + 1):
                current_sub = s[start:end]
                if is_palindrome(current_sub):
                    path.append(current_sub)
                    backtrack(end, path)
                    path.pop()
                    
        backtrack(0, [])
        return result

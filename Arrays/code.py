class Solution(object):
    def smallestNumber(self, num, t):
        temp = t
        for f in [2, 3, 5, 7]:
            while temp % f == 0:
                temp //= f
        if temp > 1:
            return "-1"
            
        n = len(num)
        
        def min_digits_needed(c2, c3, c5, c7):
            c2 = max(0, c2)
            c3 = max(0, c3)
            c5 = max(0, c5)
            c7 = max(0, c7)
            
            cnt9 = c3 // 2
            r3 = c3 % 2
            
            cnt8 = c2 // 3
            r2 = c2 % 3
            
            extra = 0
            if r3 == 1 and r2 == 1:
                extra = 1
            elif r3 == 1 and r2 == 2:
                extra = 2
            elif r3 == 1 and r2 == 0:
                extra = 1
            elif r3 == 0 and r2 == 2:
                extra = 1
            elif r3 == 0 and r2 == 1:
                extra = 1
                
            return cnt9 + cnt8 + extra + c5 + c7

        def get_factors(v):
            c = [0, 0, 0, 0]
            for i, f in enumerate([2, 3, 5, 7]):
                while v % f == 0:
                    c[i] += 1
                    v //= f
            return c

        t_factors = get_factors(t)
        
        if '0' not in num:
            num_factors = [0, 0, 0, 0]
            for d in num:
                df = get_factors(int(d))
                for i in range(4):
                    num_factors[i] += df[i]
            if all(num_factors[i] >= t_factors[i] for i in range(4)):
                return num

        prefix_factors = [0, 0, 0, 0]
        valid_prefix = True
        prefixes = []
        
        for i in range(n):
            if not valid_prefix:
                break
            prefixes.append((i, list(prefix_factors)))
            d = int(num[i])
            if d == 0:
                valid_prefix = False
                break
            df = get_factors(d)
            for k in range(4):
                prefix_factors[k] += df[k]
                
        for i in range(n - 1, -1, -1):
            if i >= len(prefixes):
                continue
            idx, p_facs = prefixes[i]
            start_d = int(num[idx]) + 1
            for d in range(start_d, 10):
                df = get_factors(d)
                rem_facs = [t_factors[k] - (p_facs[k] + df[k]) for k in range(4)]
                rem_len = n - 1 - idx
                if min_digits_needed(*rem_facs) <= rem_len:
                    c2, c3, c5, c7 = [max(0, x) for x in rem_facs]
                    digits = []
                    digits.extend([7] * c7)
                    digits.extend([5] * c5)
                    
                    cnt9 = c3 // 2
                    r3 = c3 % 2
                    cnt8 = c2 // 3
                    r2 = c2 % 3
                    
                    digits.extend([9] * cnt9)
                    digits.extend([8] * cnt8)
                    
                    if r3 == 1 and r2 == 1:
                        digits.append(6)
                    elif r3 == 1 and r2 == 2:
                        digits.extend([6, 2])
                    elif r3 == 1 and r2 == 0:
                        digits.append(3)
                    elif r3 == 0 and r2 == 2:
                        digits.append(4)
                    elif r3 == 0 and r2 == 1:
                        digits.append(2)
                        
                    digits.sort()
                    ones_needed = rem_len - len(digits)
                    suffix = ['1'] * ones_needed + [str(x) for x in digits]
                    return num[:idx] + str(d) + "".join(suffix)
                    
        req_len = max(n + 1, min_digits_needed(*t_factors))
        c2, c3, c5, c7 = [max(0, x) for x in t_factors]
        digits = []
        digits.extend([7] * c7)
        digits.extend([5] * c5)
        cnt9 = c3 // 2
        r3 = c3 % 2
        cnt8 = c2 // 3
        r2 = c2 % 3
        digits.extend([9] * cnt9)
        digits.extend([8] * cnt8)
        if r3 == 1 and r2 == 1: digits.append(6)
        elif r3 == 1 and r2 == 2: digits.extend([2, 6])
        elif r3 == 1 and r2 == 0: digits.append(3)
        elif r3 == 0 and r2 == 2: digits.append(4)
        elif r3 == 0 and r2 == 1: digits.append(2)
        
        digits.sort()
        ones_needed = req_len - len(digits)
        return '1' * ones_needed + "".join(str(x) for x in digits)

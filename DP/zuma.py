from collections import deque

class Solution:
    def findMinStep(self, board, hand):
        def clean(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    return clean(s[:i] + s[j:])
                i = j
            return s

        def get_hand_count(h):
            cnt = [0] * 26
            for c in h:
                cnt[ord(c) - ord('A')] += 1
            return tuple(cnt)

        initial_hand = get_hand_count(hand)
        queue = deque([(board, initial_hand, 0)])
        visited = {(board, initial_hand)}

        while queue:
            curr_board, curr_hand, steps = queue.popleft()
            
            if not curr_board:
                return steps

            for i in range(len(curr_board) + 1):
                for c_idx in range(26):
                    if curr_hand[c_idx] > 0:
                        char = chr(ord('A') + c_idx)
                        
                        is_worthy = False
                        if i < len(curr_board) and curr_board[i] == char:
                            is_worthy = True
                        elif i > 0 and curr_board[i-1] == char:
                            is_worthy = True
                        elif i > 0 and i < len(curr_board) and curr_board[i-1] != curr_board[i]:
                            is_worthy = True
                            
                        if not is_worthy:
                            continue

                        next_board = clean(curr_board[:i] + char + curr_board[i:])
                        
                        next_hand_list = list(curr_hand)
                        next_hand_list[c_idx] -= 1
                        next_hand = tuple(next_hand_list)

                        if (next_board, next_hand) not in visited:
                            visited.add((next_board, next_hand))
                            queue.append((next_board, next_hand, steps + 1))
                            
        return -1

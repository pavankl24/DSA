class Solution(object):

    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        extended_colors = colors + colors[: k - 1]
        count = 0
        current_length = 1

        for i in range(1, len(extended_colors)):
            if extended_colors[i] != extended_colors[i - 1]:
                current_length += 1
            else:
                current_length = 1

            if current_length >= k:
                count += 1

        return count

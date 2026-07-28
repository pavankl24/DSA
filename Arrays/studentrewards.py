class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        pos_set = set(positive_feedback)
        neg_set = set(negative_feedback)
        scores = []
        
        for rep, sid in zip(report, student_id):
            score = 0
            for word in rep.split():
                if word in pos_set:
                    score += 3
                elif word in neg_set:
                    score -= 1
            scores.append((score, sid))
            
        scores.sort(key=lambda x: (-x[0], x[1]))
        return [sid for _, sid in scores[:k]]

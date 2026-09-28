class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_count = Counter(s1)
        for start in range(len(s2) - window_size + 1):
            current_window = s2[start : start + window_size]
            current_count = Counter(current_window)
            if current_count == s1_count:
                return True

        return False

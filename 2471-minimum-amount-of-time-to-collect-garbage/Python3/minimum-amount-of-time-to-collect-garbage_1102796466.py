class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_travel = [0] + list(accumulate(travel))
        m_idx, p_idx, g_idx, total = 0, 0, 0, 0
        
        for i, trash in enumerate(garbage):
            if "M" in trash: m_idx = i
            if "P" in trash: p_idx = i
            if "G" in trash: g_idx = i
            total += len(trash)

        return total + total_travel[m_idx] + total_travel[p_idx] + total_travel[g_idx]
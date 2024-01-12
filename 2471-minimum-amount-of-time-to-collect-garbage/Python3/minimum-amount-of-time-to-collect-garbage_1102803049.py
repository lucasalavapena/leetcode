class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        N = len(garbage)
        total_travel = [0] + list(accumulate(travel))
        m_idx, p_idx, g_idx = 0, 0, 0
        
        for i in range(N-1, -1, -1):
            if "M" in garbage[i] and not m_idx: m_idx = i
            if "P" in garbage[i] and not p_idx: p_idx = i
            if "G" in garbage[i] and not g_idx: g_idx = i
            if m_idx and p_idx and g_idx: break
        return sum(len(g) for g in garbage) + total_travel[m_idx] + total_travel[p_idx] + total_travel[g_idx]
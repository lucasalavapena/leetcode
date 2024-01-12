class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        N = len(garbage)
        total_travel = [0] + list(accumulate(travel))
        m_idx, p_idx, g_idx = 0, 0, 0
        
        for i in range(N-1, -1, -1):
            if not m_idx and "M" in garbage[i]: m_idx = i
            if not p_idx and "P" in garbage[i] : p_idx = i
            if not g_idx and "G" in garbage[i] : g_idx = i
            if m_idx and p_idx and g_idx: break
        return sum(len(g) for g in garbage) + total_travel[m_idx] + total_travel[p_idx] + total_travel[g_idx]
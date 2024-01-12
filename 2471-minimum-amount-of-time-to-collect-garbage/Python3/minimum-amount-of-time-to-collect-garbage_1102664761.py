class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_travel = [0] + list(accumulate(travel))
        m, p, g = (0, 0), (0, 0), (0, 0)
        for i, trash in enumerate(garbage):
            m_delta = trash.count("M")
            if m_delta:
                m = (m[0] + m_delta, i )
            p_delta = trash.count("P")
            if p_delta:
                p = (p[0] + p_delta, i )
            g_delta = trash.count("G")
            if g_delta:
                g = (g[0] + g_delta, i )
        return m[0] + p[0] + g[0] + total_travel[m[1]] + total_travel[p[1]] + total_travel[g[1]]
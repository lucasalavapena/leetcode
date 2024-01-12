class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digits_logs = []

        for log in logs:
            ident, *rest = log.split(" ")
            if rest[0][0].isdigit():
                digits_logs.append(log)
            else:
                letter_logs.append((" ".join(rest), ident, log))
        letter_logs.sort(key=lambda x: (x[0], x[1]))
        return [og_log for alpha, ident, og_log in letter_logs] + digits_logs

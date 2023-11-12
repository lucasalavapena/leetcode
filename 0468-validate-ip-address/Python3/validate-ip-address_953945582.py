LEGAL_CHAR_IPV6 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'}

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            res = queryIP.split(".")
            if len(res) == 4 and all(item.isdigit() and 0 <= int(item) <= 255 and ( (len(item) > 1 and item[0] != "0") or len(item) == 1) for item in res):
                return "IPv4"

        elif ":" in queryIP:
            res = queryIP.split(":")
            if len(res) == 8:
                done = True
                for i, item in enumerate(res):
                    if not item or len(item) >= 5 or any(c not in LEGAL_CHAR_IPV6 for c in item):               
                        done = False
                        break 
                if done:
                    return "IPv6"

        return "Neither"
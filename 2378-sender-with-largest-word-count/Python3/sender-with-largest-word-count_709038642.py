class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        sender_wc = defaultdict(int)
        max_sender = senders[0]
        max_amount = 0
        
        for message, sender in zip(messages, senders):
            sender_wc[sender] += message.count(" ") + 1
            
            if max_amount < sender_wc[sender]:
                max_amount = sender_wc[sender]
                max_sender = sender

            elif max_amount == sender_wc[sender]:
                if max_sender < sender:
                    max_sender = sender
        
        return max_sender
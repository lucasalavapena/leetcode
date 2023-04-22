from random import randint

class Codec:
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_url = f"tiny.me/{randint(0, 10000000)}"
        self.urls[short_url] = longUrl
        return short_url
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls.get(shortUrl, "")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
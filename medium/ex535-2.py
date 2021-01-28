import base64
class Codec:
    def __init__(self):
        self.data = dict()
        self.key = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.data[self.key] = longUrl
        self.key += 1
        return "http://tinyurl.com/" + base64.b64encode(str(self.key-1).encode("ascii")).decode("utf-8")

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.data[int(base64.b64decode(shortUrl.split("http://tinyurl.com/")[1]).decode("ascii"))]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
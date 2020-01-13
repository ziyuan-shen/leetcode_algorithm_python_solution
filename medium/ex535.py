class Codec:
    def __init__(self):
        self.dic = {}
        self.urls = []
        self.count = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.dic:
            self.dic[longUrl] = self.count
            self.urls.append(longUrl)
            self.count += 1
        return "http://tinyurl.com/" + str(self.dic[longUrl])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        num = int(shortUrl.split("/")[-1])
        return self.urls[num]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
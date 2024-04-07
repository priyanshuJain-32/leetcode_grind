class Codec:
    def __init__(self):
        self.decoded = defaultdict(str)
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.decoded[self.counter]=longUrl
        short = "https://tinyurl.com/{}".format(self.counter)
        self.counter += 1
        return short
        
    def decode(self, shortUrl: str) -> str:
        count = int(shortUrl.split("/")[-1])
        return self.decoded[count]
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from collections import deque
import threading
import time

class Solution:
    lock = threading.Lock()
    def getHost(self, url):
        return url.split("/")[2]
    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = {startUrl}
        host = self.getHost(startUrl)
        q = deque([startUrl])
        threads = []
        for i in range(50):
            thread = threading.Thread(target=self.crawlUrls, args=(htmlParser, host, q, visited))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        return list(visited)
        
    def crawlUrls(self, htmlParser, host, q, visited):
        while True:
            self.lock.acquire()
            if q:
                url = q.popleft()
                self.lock.release()
                result = [url for url in htmlParser.getUrls(url) if self.getHost(url) == host]
                self.lock.acquire()
                for url in result:
                    if url not in visited:
                        visited.add(url)
                        q.append(url)
                self.lock.release()
            else:
                self.lock.release()
                break
                        
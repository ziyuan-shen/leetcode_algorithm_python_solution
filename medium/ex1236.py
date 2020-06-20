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

class Solution:
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl.split("/")[2]
        def dfs(startUrl, visited):
            children = htmlParser.getUrls(startUrl)
            for neighbor in children:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if neighbor.split("/")[2] == hostname:
                        ans.append(neighbor)
                        dfs(neighbor, visited)
        ans = [startUrl]
        visited = {startUrl}
        dfs(startUrl, visited)
        return ans
from collections import defaultdict
from collections import deque
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followdic = defaultdict(set)
        self.tweets = deque([])

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        idx = -1
        ans = []
        while len(ans) < 10 and idx >= -len(self.tweets):
            if self.tweets[idx][0] in self.followdic[userId] or self.tweets[idx][0] == userId:
                ans.append(self.tweets[idx][1])
            idx -= 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followdic[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followdic[followerId]:
            self.followdic[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
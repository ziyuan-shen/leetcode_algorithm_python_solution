"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.buffer = []
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tempbuf = [""] * 4
        
        while len(self.buffer) < n:
            readnum = read4(tempbuf)
            self.buffer.extend(tempbuf[:readnum])
            if readnum < 4:
                break
        if len(self.buffer) >= n:
            for i in range(n):
                buf[i] = self.buffer.pop(0)
            return n
        else:
            ans = len(self.buffer)
            for i in range(ans):
                buf[i] = self.buffer.pop(0)
            for i in range(ans, n):
                buf[i] = ""
            del self.buffer[:]
            return ans
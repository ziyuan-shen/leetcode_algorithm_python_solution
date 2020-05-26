"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serial = []
        q = []
        if root:
            q.append((root, 1))
            serial.append(str(root.val))
            serial.append("None")
        while q:
            root, level = q.pop(0)
            if root.children:
                for child in root.children:
                    serial.append(str(child.val))
                    q.append((child, level+1))
            serial.append("None")
        while serial and serial[-1] == "None":
            serial.pop()
        return ",".join(serial)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        serial = data.split(",")
        val = serial.pop(0)
        root = Node(int(val), [])
        if serial:
            serial.pop(0)
        q = [root]
        while q:
            current_node = q.pop(0)
            while serial and serial[0] != "None":
                val = serial.pop(0)
                new_node = Node(int(val), [])
                q.append(new_node)
                if current_node.children == []:
                    current_node.children = [new_node]
                else:
                    current_node.children.append(new_node)
            if serial:
                serial.pop(0)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
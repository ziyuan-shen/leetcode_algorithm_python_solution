class FileNode:
    def __init__(self, name, isFile = False, content = "", child = {}):
        self.name = name
        self.isFile = isFile
        self.content = content
        self.child = child
        
    def ls(self):
        if self.isFile:
            return [self.name]
        else:
            return sorted(list(self.child.keys()))

class FileSystem:

    def __init__(self):
        self.root = FileNode("root", child = {})

    def ls(self, path: str) -> List[str]:
        if path == "/":
            files = []
        else:
            files = path.split("/")[1:]
        current_dir = self.root
        for file in files:
            current_dir = current_dir.child[file]
        return current_dir.ls()

    def mkdir(self, path: str) -> None:
        if path == "/":
            files = []
        else:
            files = path.split("/")[1:]
        current_dir = self.root
        for file in files:
            if file not in current_dir.child:
                current_dir.child[file] = FileNode(file, child = {})
            current_dir = current_dir.child[file]

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath == "/":
            files = []
        else:
            files = filePath.split("/")[1:]
        current_dir = self.root
        for file in files[:-1]:
            if file not in current_dir.child:
                current_dir.child[file] = FileNode(file)
            current_dir = current_dir.child[file]
        file = files[-1]
        if file not in current_dir.child:
            current_dir.child[file] = FileNode(file, isFile = True)
        current_dir.child[file].content += content

    def readContentFromFile(self, filePath: str) -> str:
        if filePath == "/":
            files = []
        else:
            files = filePath.split("/")[1:]
        current_dir = self.root
        for file in files:
            current_dir = current_dir.child[file]
        return current_dir.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
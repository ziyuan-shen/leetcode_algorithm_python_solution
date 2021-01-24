class FileSystem:

    def __init__(self):
        self.paths = {"": -1}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False
        path = path.split("/")
        if len(path) < 2:
            return False
        if "/".join(path[:-1]) in self.paths:
            self.paths["/".join(path)] = value
            return True
        return False

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
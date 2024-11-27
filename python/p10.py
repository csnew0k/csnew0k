

import os

class SimpleFileSystem:
    def __init__(self, root):
        self.root = root
        os.makedirs(root, exist_ok=True)

    def create_directory(self, path):
        os.makedirs(os.path.join(self.root, path), exist_ok=True)

    def create_file(self, path, content=""):
        full_path = os.path.join(self.root, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(content)

    def list_directory(self, path=""):
        full_path = os.path.join(self.root, path)
        return os.listdir(full_path) if os.path.exists(full_path) else []

fs = SimpleFileSystem("my_root")
fs.create_directory("dir1")
fs.create_file("dir1/file1.txt", "Hello, world!")
print(fs.list_directory("dir1"))

import os

def walk_java_files(root):
    for path, _, files in os.walk(root):
        for f in files:
            if f.endswith(".java"):
                yield os.path.join(path, f)

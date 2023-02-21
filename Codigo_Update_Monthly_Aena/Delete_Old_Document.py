import os

def Delete_Old_Document(Path):
    if os.path.exists(Path):
        os.remove(Path)
    else:
        return 0
from pathlib import Path

def pathCheckCreate(path):
    _pathCheckCreate(Path(path))

def _pathCheckCreate(path:Path,isPath=False):
    if path.is_dir() or isPath:
        innerPath = path
    else:
        innerPath = path.parent
    if innerPath.exists():
        return
    else:
        _pathCheckCreate(innerPath.parent,isPath=True)
        innerPath.mkdir()
        return
if __name__ == '__main__':
    pathCheckCreate(r"C:\Users\kanxuan\Desktop\project\self\github.io.sources\dist\a\b\index.html")

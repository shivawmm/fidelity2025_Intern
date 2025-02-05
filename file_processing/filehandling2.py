import os

root_dir = "E:\\form filling details"
for root, dirs, files in os.walk(root_dir):
    print(f"Root directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print()

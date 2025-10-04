from pathlib import Path

# Paths and Directories
# Absolute path
    # c:\Program Files\Microsoft
# Relative path

# Methods of directories
# .mkdir() -- create directory
# .rmdir() -- remove directory
# .glob('') -- search for files and dir in current path
    # *     -- all files and dir
    # *.*   -- all files
    # *.py  -- all python files
    # *.xls -- all excel files

path = Path("packages")
print(path.exists)

path = Path("emails")
print(path.mkdir) 
print(path.rmdir) 

path = Path()
for file in path.glob('*.py'):
    print(file)
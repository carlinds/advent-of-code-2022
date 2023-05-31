from utils import *


sample1 = r"""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
sample2 = r""""""
sample3 = r""""""

actual_input = read_input()


class Folder():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def get_size(self, folders):
        return self.size + sum([folders[c].get_size(folders) for c in self.children])


def run_on_input(ipt):
    folders = {}
    current_path = ""

    for line in ipt.splitlines():
        match line.split():
            case[]:
                continue

            case["$", "ls"]:
                continue

            case["$", "cd", ".."]:
                current_path = folders[current_path].parent
                continue

            case["$", "cd", folder_name]:
                new_path = current_path + "/" + folder_name
                folders[new_path] = Folder(name=folder_name, parent=current_path)
                current_path = new_path
                continue

            case["dir", folder_name]:
                folders[current_path].children.append(current_path + "/" + folder_name)
                continue

            case[size, filename]:
                folders[current_path].size += int(size)
                continue

    dir_sizes = [f.get_size(folders) for f in folders.values()]
    space_needed = 30000000 - (70000000 - max(dir_sizes))
    print(min([s for s in dir_sizes if s >= space_needed]))
    

for ipt in [sample1, sample2, sample3, actual_input]:
    if ipt:
        run_on_input(ipt)

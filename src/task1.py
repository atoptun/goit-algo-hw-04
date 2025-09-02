import argparse
import os
import shutil
import hashlib
from pathlib import Path



parser = argparse.ArgumentParser(description="File orginizer")
parser.add_argument("source", type=str, help="Source dir")
parser.add_argument("-d", "--dest", type=str, help="Destination dir", default="dest", dest="dest")
parser.add_argument("-V", "--verbose", action="store_true", help="Verbose", default=False)

args = parser.parse_args()
# print(args.source, args.dest, args.verbose)


def print_log(line: str):
    """Print a log line if verbose"""
    if args.verbose:
        print(line)


def get_file_md5(file: Path):
    """Returns MD5 of a file"""
    func = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            func.update(chunk)
    return func.hexdigest()


def copy_file(file: Path, dest_dir: Path):
    """Copy a file to a dest folder and check dublicates"""
    ext = file.suffix if file.suffix else 'unknow'
    dir = dest_dir / ext.strip('.')
    try: 
        if not dir.exists():
            print_log(f'Create dir "{dir}"')
            os.makedirs(dir, exist_ok=True)
        file_dest = dir / file.name
        if file_dest.exists():
            hash_s = get_file_md5(file)
            if hash_s == get_file_md5(file_dest):
                print_log(f'Dublicate file "{file_dest}" from "{file}"')
                return
            tmp_name = file_dest.stem
            ind = 0
            file_dest = file_dest.with_stem(f'{tmp_name}_copy_{ind}')
            while file_dest.exists():
                if hash_s == get_file_md5(file_dest):
                    print_log(f'Dublicate file "{file_dest}" from "{file}"')
                    return
                ind += 1
                file_dest = file_dest.with_stem(f'{tmp_name}_copy_{ind}')
        print_log(f'Copy file "{file}" to {file_dest}')
        shutil.copy(file, file_dest)
    except IOError as e:
        print(f'Copy file error "{file}": {e}')



def scan_dir_tree(path: str | Path, dest_dir: Path):
    """Scans a directory tree using recursion"""
    try:
        path = Path(path)
        print_log(f'Scan dir "{path}"')
        for item in path.iterdir():
            if item.is_dir():
                scan_dir_tree(item, dest_dir)
            elif item.is_file():
                copy_file(item, dest_dir)
    except OSError as e:
        print(f"Error '{path}': {repr(e)}")



def main():
    source = args.source
    dest = args.dest

    cwd = Path.cwd()
    source = Path(source)
    dest = Path(dest)

    if not (source.exists() and source.is_dir()):
        print(f'Source MUST BE a folder and exists ({source})')
        return
    if dest.exists() and not dest.is_dir():
        print(f'Destination MUST BE a folder ({dest})')
        return
    if not dest.is_absolute():
        dest = cwd / dest

    scan_dir_tree(source, dest)
    print()


if __name__ == "__main__":
    main()
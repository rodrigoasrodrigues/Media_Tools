import argparse
from os import walk

parser = argparse.ArgumentParser(description='Find duplicated media files with different extensions at the same level.')
parser.add_argument('--path', '-p', default=None, help='root folder for the search')
args = parser.parse_args()

media_files = []
subs_files = []
media_formats = ['mp4','mkv','avi','mpeg','mpg','mov']
subs_formats = ['sub','srt','ass']
for (dirpath, dirnames, filenames) in walk(args.path):
    for fname in filenames:
        nameparts = fname.split('.')
        partsnum = len(nameparts)
        base_fname = '.'.join(nameparts[0:(partsnum-1)])
        ext = nameparts[-1]

        if ext in media_formats:
            if base_fname in media_files:
                print(f'Duplicated media file: {fname} : {base_fname}')
            else:
                media_files.append(base_fname)
        elif ext in subs_formats:
            if partsnum>2 and nameparts[-2].startswith('po'):
                base_fname = '.'.join(nameparts[0:(partsnum-2)])
            if base_fname in subs_files:
                print(f'Duplicated subs file: {fname}')
            else:
                subs_files.append(base_fname)



from typing import Union
from pathlib import Path
from PIL import ImageOps, Image

def exif_transpose_folder(folder: Union[str, Path], recursive = False, verbose=False):
    folder = Path(folder)
    if verbose:
        print(f"Transposing pictures of folder \"{folder}\"")
    for entry in folder.iterdir():
        if entry.is_dir() and recursive:
            exif_transpose_folder(entry, recursive=True, verbose=verbose)
        else:
            try:
                if verbose:
                    print(f"Transposing file \"{entry}\"")
                image=Image.open(entry)
                image = ImageOps.exif_transpose(image)
                image.save(entry)
            except Exception as e:
                if verbose:
                    print(e)
#!/usr/bin/env python3

import os
import subprocess
import sys
from importlib.resources import files
from tempfile import TemporaryDirectory


def _create_vimrc_file(directory: str) -> str:
    vimrc = files("vik").joinpath(".vimrc").read_text()
    vimrc_path = os.path.join(directory, ".vimrc")
    with open(vimrc_path, "w") as f:
        f.write(vimrc)
    return vimrc_path


def main():
    with TemporaryDirectory() as tmp_dir:
        vimrc_path = _create_vimrc_file(tmp_dir)
        subprocess.run(["vim", "-u", vimrc_path, sys.argv[1]])


if __name__  == "__main__":
    main()
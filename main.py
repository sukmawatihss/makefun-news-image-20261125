# THE SOUTHERN WIRE - NI25 entry program for Akun 15 (sukmawatihss).
# Python standard library only. Copy-only: writes the embedded entry.png
# to /output/entry.png, byte-identical on every run. No network, no PIL.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()

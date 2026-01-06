import argparse

from app.Assembler import Assembler

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str)
    args = parser.parse_args()

    a = Assembler()
    a.run(args.file_name)

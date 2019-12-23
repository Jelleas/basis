import argparse
import basis
import basis.logger as logger

def main():
    parser = argparse.ArgumentParser(prog="basis")
    parser.add_argument("file",
                        help="file to execute")
    parser.add_argument("-v", "--verbose",
                        action="store_true",
                        help="print the code and the log")
    args = parser.parse_args()

    if args.verbose:
        with open(args.file) as f:
            print(f.read())
        logger.enable()

    output = basis.interpret(args.file)

    for line in output:
        print(line)

if __name__ == "__main__":
    main()

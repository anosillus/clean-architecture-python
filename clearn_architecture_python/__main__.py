import sys

from clearn_architecture_python.clearn_architecture_python import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))

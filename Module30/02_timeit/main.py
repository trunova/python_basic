import timeit
import time


if __name__ == "__main__":
    res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(res)
    start = time.time()
    string = "-".join(["-".join([str(n) for n in range(0, 100)]) for i in range(10000)])
    print(time.time() - start)
    start = time.time()
    string = "-".join(["-".join(list(map(lambda n: str(n), [n for n in range(0, 100)]))) for i in range(10000)])
    print(time.time() - start)

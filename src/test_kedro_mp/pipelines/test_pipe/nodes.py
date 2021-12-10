from typing import List
import multiprocessing as mp


def _my_func(x: int) -> int:
    return x ** x


# Prepare node
def test_mp() -> List[int]:
    integer_list = [1, 2, 3, 4]
    pool = mp.Pool(mp.cpu_count())
    res = pool.map(_my_func, integer_list)
    print(res)
    return res

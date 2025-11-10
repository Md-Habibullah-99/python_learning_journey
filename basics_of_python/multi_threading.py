import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
  print(f"sleeping for {seconds} seconds\n")
  time.sleep(seconds)
  return seconds


def main():
  time1 = time.perf_counter()
  # Normal code
  # func(2)
  # func(2)
  # func(2)

  # same code using threads
  t1 = threading.Thread(target=func, args=[2])
  t2 = threading.Thread(target=func, args=[4])
  t3 = threading.Thread(target=func, args=[3])

  t1.start()
  t2.start()
  t3.start()

  t1.join()
  t2.join()
  t3.join()
  time2 = time.perf_counter()
  print("\n",time2-time1)


def poolingDemo():
  with ThreadPoolExecutor(max_workers=1) as executor:
    # future = executor.submit(func,  3)
    # print(future.result())
    # future = executor.submit(func,  2)
    # print(future.result())
    # future = executor.submit(func,  6)
    # print(future.result())
    
    # future1 = executor.submit(func,  3)
    # future1 = executor.submit(func,  2)
    # future1 = executor.submit(func,  6)
    # print(future1.result())
    # print(future1.result())
    # print(future1.result())
    l = [2,1,3,5,6,9,4]
    results = executor.map(func, l)
    for result in results:
      print(result)

poolingDemo()



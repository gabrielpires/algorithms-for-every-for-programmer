import time


def execution_time(start):
    seconds = round(time.time() - start, 2)
    print('Executed in:', seconds, ' seconds')

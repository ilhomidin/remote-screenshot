"""
Run remscreen without any output.
"""
from multiprocessing import Process

from remscreen import client


if __name__ == '__main__':
    p = Process(target=client.run_until_disconnected, name="remscreen", daemon=True)
    p.start()

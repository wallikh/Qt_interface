import time
import asyncio
import concurrent.futures


class TaskSynchronizer():
    """
    A simple concurrent tasks synchornizer
    """

    def __init__(self, max_workers=5):
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=max_workers)

    def __worker(self, *args):
        delay_exe = args[0][0]
        func = args[0][1]
        time.sleep(delay_exe)
        return func()

    async def __non_blocking(self, tasks):
        loop = asyncio.get_event_loop()
        fs = []
        for task in tasks:
            fs.append(loop.run_in_executor(
                self.executor, self.__worker, task))
        done, pending = await asyncio.wait(fs=fs, return_when=asyncio.ALL_COMPLETED)
        results = [task.result() for task in done]
        return results

    def sync(self, tasks):
        """
        call this function with multiple tasks to run concurrently.
        tasks is a list of (delay, lamda function) tuple. for exmaple:
        tasks = [ (0, lambda: print("hello")), (3, lambda: print("world")), ...]
        returns a list of each lamda function return value
        """
        results = asyncio.run(self.__non_blocking(tasks))
        return results
import logging
import queue
import random
import string
import threading
import unittest

"""
You can use any module you want. Write a service that runs two asynchronous loops,
 one produces a random message and puts it into a queue. Another, reads from the queue and threads a worker process to
 write that message into a log file. The worker process should only thread a max of 20 threads.
"""


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',)


class AsynchronousLoops(object):
    def __init__(self):
        self.q = queue.Queue(maxsize=0)

    """
    This method is generating the random 
     string and adding it to the queue.

    @param number: length of the message
    """
    @staticmethod
    def random_message_generator(number, q):
        q.put(
            ''.join(random.choice(
                string.ascii_letters) for _ in range(number)))

    """
    This method is getting the string message and debugging it.
    """
    def logging_queue(self):
        while not self.q.empty():
            random_message = self.q.get()
            logging.debug(random_message)
            self.q.task_done()

    """
    This method is running threads for getting the message from worker
    
    @param thread_max_number: Maximum number of threads
    @param string_length: length of the message
    """
    def running_thread(self, thread_max_number, string_length):
        num_threads = thread_max_number
        for i in range(num_threads):
            thread1 = threading.Thread(name='random_message_generator', target=self.random_message_generator,
                                       args=(string_length, self.q))
            thread1.start()
            thread2 = threading.Thread(name='logging_queue', target=self.logging_queue)
            thread2.start()


if __name__ == '__main__':
    async = AsynchronousLoops()
    async.running_thread(20, 32)

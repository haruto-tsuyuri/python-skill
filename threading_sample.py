import gevent

import threading
import redis
import os

conn = redis.Redis()
print(os.getpid())


def do_this(what):
    whoami(what)


def whoami(what):
    print(f'Thread {threading.current_thread()} says : {what}')


whoami("I'm the main program")
for n in range(4):
    p = threading.Thread(target=do_this, args=(n,))
    p.start()


# gevent

def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(2)
    print('Implicit context switch back to bar')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])

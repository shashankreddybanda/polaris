from flask import Flask, request
import redis
from rq import Queue

import time

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)


def backgroundTask(n):

    delay = 2
    
    print("task running")
    print(f"simulating {delay} seconds delay")

    time.sleep(delay)

    print(len(n))
    print("'''task complete'''")
    return len(n)


@app.route("/task")
def addTask():

    if request.args.get("n"):

        job = q.enqueue(backgroundTask, request.args.get("n"))

        return f"Task {job.id} added to queue at {job.enqueued_at}. {len(q)} tasks are in the queue "

    return "No value for n"


if __name__ == "__main__":
    app.run()

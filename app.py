from flask import Flask, request
import redis
from rq import Queue
from background_task import backgroundTask

import time

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)


@app.route("/task")
def addTask():

    if request.args.get("n"):

        job = q.enqueue(backgroundTask, request.args.get("n"))

        return f"Task {job.id} added to queue at {job.enqueued_at}. {len(q)} tasks are in the queue "

    return "No value for n"


if __name__ == "__main__":
    app.run()

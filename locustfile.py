#!/usr/bin/env python

from locust import HttpLocust, TaskSet, task
from random import Random

class FizzBuzzTasks(TaskSet):

    @task
    def ping(self):
        self.client.get("/ping")
        
    @task
    def about(self):
        n = Random()
        self.client.get("/query/%s" % str(n.randint(8,25)))

class FizzBuzzUser(HttpLocust):
    task_set = FizzBuzzTasks
    min_wait = 50
    max_wait = 1500

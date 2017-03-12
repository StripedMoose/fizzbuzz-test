#!/usr/bin/env python

from locust import HttpLocust, TaskSet


def index(l):
    l.client.get("/")

def ping(l):
    l.client.get("/ping")


class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

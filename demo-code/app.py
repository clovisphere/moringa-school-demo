from locust import HttpLocust, TaskSet, task

MIN_WAIT_TIME = 5000
MAX_WAIT_TIME = 5000

class UserAction(TaskSet):

    @task(1)
    def apply(self):
        self.client.get('/apply-now')
    
    @task(2)
    def prep_info(self):
        self.client.get('/prep')
    
    @task(1)
    def program_overview(self):
        self.client.get('/overview')

class User(HttpLocust):
    task_set = UserAction
    min_wait = MIN_WAIT_TIME
    max_wait = MAX_WAIT_TIME

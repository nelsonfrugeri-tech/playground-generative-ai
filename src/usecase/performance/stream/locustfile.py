from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def hello_world(self):
        self.client.get("/")

    @task(3)
    def view_stream(self):
        self.client.get("/stream")

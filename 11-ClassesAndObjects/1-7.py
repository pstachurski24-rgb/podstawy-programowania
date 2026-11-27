# 1-7: Social media timeline
# NOTE: Original socialmedia.py was not provided; this is an independent implementation.
class SocialMedia:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, text):
        self.posts.append(text)

    def display_timeline(self):
        print(f"Timeline for {self.username}:")
        for number, post in enumerate(self.posts, start=1):
            print(f"{number}. {post}")

user = SocialMedia("johndoe")
user.add_post("Hello, world!")
user.add_post("Had a great day at the park!")
user.add_post("What's up, Natalie? How are you?")
user.display_timeline()

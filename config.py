import os

class Config(object):
    API_KEY = os.environ.get('API_KEY') or 'AIzaSyDGhb7J_7ElftJMq1Q42XT27yiYckppDjo'

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
# SECRET_KEY = 'R\\A(I>m_lwwxqp.x^yX*j/]:'


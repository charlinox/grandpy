import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'R\\A(I>m_lwwxqp.x^yX*j/]:'

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
# SECRET_KEY = 'R\\A(I>m_lwwxqp.x^yX*j/]:'


import os


class Config(object):
    API_KEY_BACK = os.environ.get('API_KEY_BACK')
    API_KEY_FRONT = os.environ.get('API_KEY_FRONT')
    SECRET_KEY = 'R\\A(I>m_lwwxqp.x^yX*j/]:'
# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
# SECRET_KEY = 'R\\A(I>m_lwwxqp.x^yX*j/]:'

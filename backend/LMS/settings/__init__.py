from decouple import config
env=config("ENV", None)

if env=='prod':
    from .production import *
else:
    from .development import *
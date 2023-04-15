import os
from pathlib import Path
from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings')

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / 'static'

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_DIR)
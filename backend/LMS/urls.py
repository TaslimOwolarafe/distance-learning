from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path("teachers/", include('teachers.urls')),
    path("classes/", include('classes.urls')),
    path('students/', include('students.urls')),
    path('assignments/', include('assignments.urls')),
    path('announcements/', include('announcements.urls')),
    path('quizzes/', include('quizzes.urls'))
]

urlpatterns+=[
    path('api-auth/', include('rest_framework.urls'),),
]

if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
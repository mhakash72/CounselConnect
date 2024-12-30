from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
# path('accounts/', include('apps.accounts.urls')),
# path('chambers/', include('apps.chambers.urls')),
# path('barristers/', include('apps.barristers.urls')),
# path('bookings/', include('apps.bookings.urls')),
# path('practice-areas/', include('apps.practice_areas.urls')),
# path('cms/', include('apps.cms.urls')),
# path('', include('apps.core.urls')),
]
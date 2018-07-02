import re
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'', include('membership.urls')),
]

# urlpatterns = [
#     #path('', views.home, name='home'),
    
#     url(r'^$', 'membership.views.home', name='home'),
# ]

# urlpatterns = [
#     url(r'^$', 'membership.views.home', name='home'),
#     url(r'^admin/', include(admin.site.urls)),
# ]

# urlpatterns += [
#     url(r'^membership/', include('membership.urls')),
# ]

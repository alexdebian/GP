"""gpproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from gpproject import settings
from galery.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^galery/$', upload_files, name='upload_files'),
    url(r'^galery/(?P<username>\w+)/$', other_user_profile, name='other_user_profile'),

    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register, name='register'),

    url(r'^password_change/$', change_password, name='password_change'),

    url(r'^reset/password_reset/$', reset_password, name='password_reset'),
    url(r'^reset/password_reset/done/$', PasswordResetDone.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^reset/done/$', reset_password_complete, name='password_reset_complete'),

    url(r'^account/$', Profile.as_view(), name='profile'),
    url(r'^account/update/(?P<pk>\d+)/$', UsersUpdate.as_view(), name='update'),
    url(r'^$', HomeView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

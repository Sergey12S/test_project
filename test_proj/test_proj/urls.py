"""test_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.decorators import user_passes_test
from test_app.views import Index, UsersList, SignUp, UserDetail, UserDelete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$|index/$', Index.as_view()),
    url(r'^users_list/$', user_passes_test(lambda u: u.is_superuser)(UsersList.as_view())),
    url(r'^user_detail/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_superuser)(UserDetail.as_view()), name='user_detail'),
    url(r'^user_detail/(?P<pk>\d+)/delete/$', user_passes_test(lambda u: u.is_superuser)(UserDelete.as_view()), name='user_delete'),
    url(r'^sign_in/$', login, {'template_name': 'sign_in.html'}),
    url(r'^sign_up/$', SignUp.as_view()),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


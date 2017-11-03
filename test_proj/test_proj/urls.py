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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import user_passes_test
from test_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$|index/$', Index.as_view()),
    url(r'^users_list/$', user_passes_test(lambda u: u.is_superuser)(UsersList.as_view())),
    url(r'^user_detail/(?P<pk>\d+)/$', user_passes_test(lambda u: u.is_superuser)(UserDetail.as_view()), name='user_detail'),
    url(r'^user_detail/(?P<pk>\d+)/delete/$', user_passes_test(lambda u: u.is_superuser)(UserDelete.as_view()), name='user_delete'),
    url(r'^sign_in/$', login, {'template_name': 'sign_in.html'}),
    url(r'^logout/$', logout),
    url(r'^sign_up/$', SignUp.as_view()),
    url(r'^export/xls/$', export_users_xls, name='export_users_xls'),
    url(r'^voting/$', VotingList.as_view(), name='voting'),
    url(r'^voting/(?P<pk>\d+)/like/$', login_required(ImageLike.as_view()), name='image_like'),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

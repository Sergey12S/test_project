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
from django.conf import settings
from django.conf.urls.static import static
from test_app.views import *
from test_app.api import ClientViewSet, LikeAjaxAPIView
from rest_framework import routers


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$|list_clients/$', ListClientsView.as_view()),
    url(r'^list_clients/(?P<pk>\d+)/$', DetailClientView.as_view(),
        name='detail_client'),
    url(r'^list_clients/(?P<pk>\d+)/delete/$', DeleteClientView.as_view(),
        name='delete_client'),
    url(r'^export/xls/$', export_users_xls, name='export_users_xls'),
    url(r'^voting/$', VotingListView.as_view(), name='voting'),
    url(r'^add_client/$', AddClientView.as_view()),
    url(r'^voting/(?P<pk>\d+)/like/$', LikeUserView.as_view(),
        name='like'),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^clients/(?P<pk>\d+)/like/$', LikeAjaxAPIView.as_view(),
        name='like_ajax'),
]

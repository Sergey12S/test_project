from django.conf.urls import url
from test_app.api import LikeAjaxAPIView


urlpatterns = [
    url(r'^(?P<pk>\d+)/like/$', LikeAjaxAPIView.as_view(),
        name='like_ajax'),
]

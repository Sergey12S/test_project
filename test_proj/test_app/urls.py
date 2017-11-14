from django.conf.urls import url
from test_app.views import *


urlpatterns = [
    url(r'^$', ListClientsView.as_view()),
    url(r'^add/$', AddClientView.as_view()),
    url(r'^voting/$', VotingListView.as_view()),
    url(r'^export/xls/$', export_users_xls),
    url(r'^(?P<pk>\d+)/$', DetailClientView.as_view(),
        name='detail_client'),
    url(r'^(?P<pk>\d+)/delete/$', DeleteClientView.as_view(),
        name='delete_client'),
    url(r'^(?P<pk>\d+)/like/$', LikeUserView.as_view(),
        name='like'),
]

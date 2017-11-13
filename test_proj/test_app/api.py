from django.db import transaction
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .serializers import ClientSerializer
from .models import Client
from .views import LikeMixin


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all().order_by("-id")
    serializer_class = ClientSerializer


@method_decorator(transaction.atomic, name="get")
class LikeAjaxAPIView(LikeMixin, RetrieveAPIView):
    queryset = Client.objects.all()

    def get(self, request, *args, **kwargs):
        self.like()
        return Response(self.get_object().rating)

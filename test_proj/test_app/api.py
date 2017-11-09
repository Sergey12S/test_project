from django.db.models import F
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer
from .models import Client


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all().order_by("-id")
    serializer_class = ClientSerializer


class LikeAjaxAPIView(APIView):

    def get(self, request, *args, **kwargs):
        Client.objects.select_for_update().\
            filter(rating__lt=10, pk=self.kwargs["pk"]).\
            update(rating=F("rating") + 1)
        return Response(status=status.HTTP_200_OK)

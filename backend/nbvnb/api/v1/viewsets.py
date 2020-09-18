from rest_framework import authentication
from nbvnb.models import Bngvnbvnb
from .serializers import BngvnbvnbSerializer
from rest_framework import viewsets


class BngvnbvnbViewSet(viewsets.ModelViewSet):
    serializer_class = BngvnbvnbSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Bngvnbvnb.objects.all()

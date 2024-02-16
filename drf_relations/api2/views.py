from rest_framework.viewsets import ModelViewSet

# from .models import Singer,Song
from .serializers import SingerSerializer,SongSerializer
from api.models import Singer,Song

# Create your views here.
class SingerAPI2(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongAPI2(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
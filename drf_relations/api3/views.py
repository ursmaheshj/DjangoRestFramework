from rest_framework.viewsets import ModelViewSet

# from .models import Singer,Song
from .serializers import SingerSerializer,SongSerializer
from api.models import Singer,Song

# Create your views here.
class SingerAPI3(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongAPI3(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
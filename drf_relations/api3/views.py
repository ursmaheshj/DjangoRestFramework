from rest_framework.viewsets import ModelViewSet

# from .models import Singer,Song
from .serializers import SingerSerializer,SongSerializer
from .models import Singer,Song

# Create your views here.
class SingerAPI(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongAPI(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
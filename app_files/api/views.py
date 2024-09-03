from rest_framework import generics
from ..models import SourceFiles
from ..serializers import SourceFilesSerializer
from rest_framework.permissions import IsAuthenticated

class SourceFilesListView(generics.ListAPIView):
    queryset = SourceFiles.objects.exclude(map__isnull=True, user__isnull=True)
    serializer_class = SourceFilesSerializer
    #permission_classes = [IsAuthenticated]
    #def get_queryset(self):
    #    return SourceFiles.objects.filter(user=self.request.user)

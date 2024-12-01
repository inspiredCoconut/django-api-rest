from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter


class ListCreateMovieAPIView(ListCreateAPIView):
    """
    View for listing and creating movies
    
    Methods:
        - get: Lists all movies
        - post: Creates a new movie
        
    """
    
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting movies
    
    Methods:
        - get: Retrieves a movie
        - put: Updates a movie
        - delete: Deletes a movie
        
    """
    
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
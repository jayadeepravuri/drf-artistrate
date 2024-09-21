
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Art
from .serializers import ArtSerializer
from drf_artistrate.permissions import IsOwnerOrReadOnly



class ArtList(generics.ListCreateAPIView):
    queryset = Art.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    serializer_class = ArtSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'category',
        'tagged_user__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',
        'tagged_user__username',
        'description',
        'created_at',
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)


class ArtDetail(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Art.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    serializer_class = ArtSerializer
    permission_classes = [IsOwnerOrReadOnly]
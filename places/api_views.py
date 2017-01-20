from rest_framework import generics
from .models import Feature, Collection
from .serializers import CollectionSerializer, FeatureSerializer
from django.contrib.gis.geos import Polygon

class CollectionListView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class FeatureListView(generics.ListCreateAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self):
        collection_id = self.kwargs['collection_id']
        params = self.request.GET.dict()
        qset = Feature.objects.filter(collection_id=collection_id)
        if 'bbox' in params and params['bbox']:
            bbox_filter = params['bbox']
            bbox = Polygon.from_bbox((float(b) for b in bbox_filter.split(',')))
            qset = qset.filter(geometry__bboverlaps=bbox)
        return qset


class FeatureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self):
        collection_id = self.kwargs['collection_id']
        return Feature.objects.filter(collection_id=collection_id)

    def get_object(self):
        pk = self.kwargs['pk']
        return Feature.objects.get(pk=pk)



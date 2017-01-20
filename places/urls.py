from django.conf.urls import url, include
from django.contrib import admin
from .api_views import CollectionListView, CollectionDetailView, FeatureListView, FeatureDetailView

urlpatterns = [
    url('^collections$', CollectionListView.as_view(), name='collections_view'),
    url('^collections/(?P<pk>[0-9a-f\-]{36})$', CollectionDetailView.as_view(), name='collection_view'),
    url('^collections/(?P<collection_id>[0-9a-f\-]{36})/features$', FeatureListView.as_view(), name='features_view'),
    url('^collections/(?P<collection_id>[0-9a-f\-]{36})/features/(?P<pk>[0-9a-f\-]{36})', FeatureDetailView.as_view(), name='feature_view'),
]
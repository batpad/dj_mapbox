from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Feature, Collection


class FeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'properties', 'geometry',)
        geo_field = 'geometry'

    def get_properties(self, instance, fields):
        props = instance.properties
        if instance.name:
            props['name'] = instance.name
        return props

    def unformat_geojson(self, feature):
        attrs = {
            self.Meta.geo_field: feature["geometry"],
            "properties": feature["properties"]
        }
        if "name" in feature["properties"]:
            attrs['name'] = feature["properties"]["name"]

        return attrs


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'features', 'name', 'description',)

    features = FeatureSerializer(many=True)

    def create(self, validated_data):
        features_data = validated_data.pop('features')
        collection = Collection.objects.create(**validated_data)
        for feature_data in features_data:
            Feature.objects.create(collection=collection, **feature_data)
        return collection


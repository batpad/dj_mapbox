from django.contrib import admin
from .models import Feature, Collection

class FeatureInline(admin.StackedInline):
    model = Feature

class CollectionAdmin(admin.ModelAdmin):
    inlines = [
        FeatureInline
    ]

admin.site.register(Collection, CollectionAdmin)
# Generated by Django 2.0 on 2017-01-20 06:34

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('properties', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Collection')),
            ],
        ),
    ]
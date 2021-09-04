from rest_framework import serializers
from searches.models import SavedSearch


class SavedSearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SavedSearch
        fields = ['search_text', 'created']

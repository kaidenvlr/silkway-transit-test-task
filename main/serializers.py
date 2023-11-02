from rest_framework import serializers

from main.models import LocomotivePart


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class LocomotivePartSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = LocomotivePart
        fields = ('id', 'schema_id', 'parent', 'russian_name', 'chinese_name', 'quantity', 'description', 'children')

from rest_framework import serializers


class CurrencySerializer(serializers.Serializer):
   amount_from = serializers.IntegerField()
   to = serializers.CharField(max_length=255)
   from_ = serializers.CharField(max_length=255)
   amount_to = serializers.CharField()
   date = serializers.DateField()



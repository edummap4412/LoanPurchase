from rest_framework import serializers


class ProfileClientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    tax_id = serializers.CharField(max_length=14)
    loan_value = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        fields = '__all__'


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=50)
    number = serializers.CharField(max_length=6)

    class Meta:
        fields = '__all__'


class RegisterSerializer(serializers.Serializer):
    client = ProfileClientSerializer(many=False)
    address = AddressSerializer(many=False)

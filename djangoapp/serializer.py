from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from pycpfcnpj import cpf
from services.profileclient_service import ProfileClientService
import logging

logger = logging.getLogger(__name__)


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

    class Meta:
        fields = '__all__'

    profile_service = ProfileClientService

    def create(self, validated_data):
        owner = validated_data['client']
        address = validated_data['address']

        try:
            if cpf.validate(owner['tax_id']):
                self.profile_service(
                    name=owner['name'],
                    tax_id=owner['tax_id'],
                    loan_value=owner['loan_value'],
                    street=address['street'],
                    state=address['state'],
                    number=address['number']
                ).create_profile()
        except ValidationError:
            raise ValidationError("Check the tax_id and try again")
        except Exception as e:
            raise e.args[0]
        return validated_data

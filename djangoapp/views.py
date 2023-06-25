from rest_framework import status, generics
from rest_framework.response import Response
from djangoapp.serializer import RegisterSerializer
from djangoapp.models import ProfileClient
from helpers.validate_cpf import validate_tax_id
from rest_framework.permissions import IsAdminUser
from djangoapp.tasks import process_loans


class RegisterClientViewSet(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return ProfileClient.objects.get()

    def create(self, request, *args, **kwargs):
        permission_classes = (IsAdminUser,)
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        owner = serializer.validated_data['client']
        address = serializer.validated_data['address']

        if validate_tax_id(owner['tax_id']):
            profile_client = ProfileClient.objects.create(
                name=owner['name'],
                tax_id=owner['tax_id'],
                loan_value=owner['loan_value'],
            )
            profile_client.addresses.create(
                street=address['street'],
                state=address['state'],
                number=address['number']
            )
            process_loans.delay()
            return Response(
                {'message': 'Usuário cadastrado com sucesso, sua solicitação de crédito está sendo avaliada'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'message': 'Não foi possivel fazer o cadatro, verifique os dados preechidos'},
            status=status.HTTP_400_BAD_REQUEST
        )


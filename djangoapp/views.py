from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from djangoapp.serializer import RegisterSerializer
from djangoapp.models import ProfileClient


class RegisterClientViewSet(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return ProfileClient.objects.get()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {'message': 'Usuário cadastrado com sucesso, sua solicitação de crédito está sendo avaliada'},
                    status=status.HTTP_201_CREATED
                )
            except ValidationError as e:
                return Response(data=e.args, status=status.HTTP_400_BAD_REQUEST)
            except Exception:
                return Response(
                    {'message': 'Não foi possivel fazer o cadatro, verifique os dados preechidos'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

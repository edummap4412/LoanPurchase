from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from djangoapp.serializer import RegisterSerializer, ProfileClientSerializer
from djangoapp.models import ProfileClient
from helpers.custom_response import CustomResponse
import os
import carbone_sdk


class RegisterClientViewSet(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return ProfileClient.objects.filter()

    def create(self, request, *args, **kwargs):
        custom_response = CustomResponse()
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            custom_response.set_form_errors(serializer.errors)
            return Response(data=custom_response.response, status=custom_response.status)

        try:
            serializer.save()
            custom_response.set_message(
                'Usuário cadastrado com sucesso, sua solicitação de crédito está sendo avaliada'
            )
            custom_response.set_status(status.HTTP_201_CREATED)
        except ValidationError as e:
            custom_response.set_message(e.args)

        except Exception:
            custom_response.set_message('Não foi possivel fazer o cadatro, verifique os dados preechidos')
            custom_response.set_status(status.HTTP_400_BAD_REQUEST)

        return Response(data=custom_response.response, status=custom_response.status)

    def list(self, request, *args, **kwargs):

        csdk = carbone_sdk.CarboneSDK("test_eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2OTkyNTc3Nzg2MDIyNzMzMzMiLCJhdWQiOiJjYXJib25lIiwiZXhwIjoyMzU1MDgxMzUzLCJkYXRhIjp7InR5cGUiOiJ0ZXN0In19.AXEhQ3aQxMk4qF9XkJJ2Fvux9477he-0oErd5sPmD5GXD0vvOMfmiupOIlrtEaxevJAgiewOXZSLmnDWzFLyxqrCAdqB9XlDU4CtLmFkfl3EL_iEJhlLvEizUWmE1wKqiztB5YohgqcwoFr_TI5ppvx9g64RcmYcbOsczpQdA-QTKK73")
        #template_path = os.path.join(os.path.dirname(__file__), 'template_report.odt')
        serializer = ProfileClientSerializer(self.get_queryset(), many=True).data
        #report_bytes, unique_report_name = csdk.render(template_path, serializer.data)

        breakpoint()
        list_profiles = [dict(s) for s in serializer]
        data = {
              "data": {
                "products": list_profiles,
                "total": sum(list(map(lambda p: float(p['loan_value']), list_profiles)))
              },
              "convertTo": "pdf"
        }
        report_bytes, unique_report_name = csdk.render("08c99383304641178bcf99cf3c11fb839cacdaa9866dbaa9e141a7b8b327add6", data)

        output_path = os.path.join(os.path.dirname(__file__), 'relatorio_gerado.pdf')
        with open(output_path, "wb") as fd:
            fd.write(report_bytes)

        return Response(data="Qualquerc")

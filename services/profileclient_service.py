from django.db import transaction, DatabaseError
from djangoapp.models import ProfileClient
import logging


logger = logging.getLogger(__name__)


class ProfileClientService(object):
    model = ProfileClient

    def __init__(self, name=None, tax_id=None, loan_value=None, status=None, street=None, state=None, number=None):
        self.name = name
        self.tax_id = tax_id
        self.loan_value = loan_value
        self.status = status
        self.street = street
        self.state = state
        self.number = number

    @transaction.atomic()
    def create_profile(self):
        try:
            if not self.model.objects.filter(tax_id=self.tax_id).exists():
                profile_client = self.model.objects.create(
                    name=self.name,
                    tax_id=self.tax_id,
                    loan_value=self.loan_value,
                    status=self.status
                )
                profile_client.addresses.create(
                    street=self.street,
                    state=self.state,
                    number=self.number
                )

        except DatabaseError as e:
            logging.error(e)
        except Exception as e:
            logging.error(e)
            raise ValueError("Não foi possivel criar o usuario")

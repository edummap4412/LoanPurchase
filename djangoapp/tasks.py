import logging
from celery import shared_task
from django.db import transaction
from .models import ProfileClient

logger = logging.getLogger(__name__)


@shared_task
def process_loans():
    profile_clients = ProfileClient.objects.filter(status=0)
    if profile_clients:
        for profile_client in profile_clients:
            loan_value = profile_client.loan_value

            if loan_value >= 5000:
                profile_client.status = ProfileClient.DENIED
                message = f"Loan value {loan_value} denied for ProfileClient {profile_client.id}"
            else:
                profile_client.status = ProfileClient.APPROVED
                message = f"Loan value {loan_value} approved for ProfileClient {profile_client.id}"

            with transaction.atomic():
                profile_client.save()

            logger.info(message)  # Adiciona um log de informação

        return "Loans processed successfully"

    return "There is no pending loan application"

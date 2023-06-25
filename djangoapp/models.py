import uuid

from django.db import models


class ProfileClient(models.Model):
    PENDING = 0
    APPROVED = 1
    DENIED = 2
    STATUS_CHOICE = (
        (APPROVED, "APROVADO"),
        (DENIED, "NEGADO"),
        (PENDING, "PENDING")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    tax_id = models.CharField(max_length=14)
    loan_value = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=PENDING, null=True, blank=True)


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=25, null=True, blank=True)
    number = models.CharField(max_length=6, null=True, blank=True)
    owner = models.ForeignKey(ProfileClient, on_delete=models.CASCADE, related_name='addresses')

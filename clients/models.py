import email
from django.db import models
from numberGenerator import generateClientNumber
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
# Create your models here.

def clientNumberGenerator():
    qs = Client.objects.order_by('-created_at')
    room_number = generateClientNumber(prefix='C', qs=qs)
    return room_number

class Client(models.Model):
    GENDER_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ]
    client_number = models.CharField(_("Client Number"), max_length=50, default=clientNumberGenerator)
    first_name = models.CharField(_("First Name"), max_length=50)
    middle_name = models.CharField(_("Middle Name"), default=' ', max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    gender = models.CharField(_("Gender"), max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(_("Age"), blank=True, null=True)
    address = models.TextField(_("Residential Address"))
    funding_account = models.ManyToManyField(
        'FundingAccount',
        verbose_name=_('Funding Accounts'),
        through='ClientFunding',
        through_fields=('client', 'fundingaccount')
    )
    is_active = models.BooleanField(_("Actiive"), default=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)


    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return f'{self.first_name + " " + self.middle_name + " " + self.last_name}'

    def get_absolute_url(self):
        return reverse("Client_detail", kwargs={"pk": self.pk})

    def get_fullname(self):
        if self.middle_name != '-':
            return f'{self.first_name + " " + self.middle_name + " " + self.last_name}'
        return f'{self.first_name + " " + self.last_name}'


class FundingAccount(models.Model):
    """Model definition for FundingAccount."""

    # TODO: Define fields here
    code = models.CharField(_("Funding Code"), max_length=50, null=True, blank=True)
    name = models.CharField(_("Name"), max_length=120)
    phone = models.CharField(_("Phone Number"), max_length=13, default=_('-'))
    email = models.EmailField(_("Email"), max_length=254, blank=True, null=True)
    country = models.CharField(_("Country"), max_length=120, default=_('-'))
    region = models.CharField(_("Region"), max_length=50, default=_('-'))
    town = models.CharField(_("Town/City"), max_length=50, default=_('-'))
    street = models.CharField(_("Street"), max_length=50, default=_('-'))
    discount = models.PositiveIntegerField(_("Discount"), default=0)

    class Meta:
        """Meta definition for FundingAccount."""

        verbose_name = 'Funding Account'
        verbose_name_plural = 'Funding Accounts'

    def __str__(self):
        """Unicode representation of FundingAccount."""
        return self.name


class ClientFunding(models.Model):
    """Model definition for ClientFunding."""
    PAYMENT_TYPE_CHOICES = [
        ('', '-----------------'),
        ('credit', 'Credit'),
        ('cash', 'Cash'),
    ]
    # TODO: Define fields here
    client = models.ForeignKey(Client, verbose_name=_("Client"), on_delete=models.CASCADE)
    fundingaccount = models.ForeignKey(FundingAccount, verbose_name=_("Funding Account"), on_delete=models.SET_NULL, null=True, blank=True)
    valid_from = models.DateTimeField(_("Validity From"), default=timezone.now)
    valid_to = models.DateTimeField(_("Validity To"), blank=True, null=True)
    is_active = models.BooleanField(_("Active"), default=True)
    discount = models.PositiveIntegerField(_("Discount"), default=0)
    payment_type = models.CharField(_("Payment Type"), max_length=10, choices=PAYMENT_TYPE_CHOICES)
    class Meta:
        """Meta definition for ClientFunding."""

        verbose_name = 'Client Funding'
        verbose_name_plural = 'Client Fundings'
        ordering = ('client',)

    def __str__(self):
        """Unicode representation of ClientFunding."""
        return f'{str(self.client) + " ---> [" + str(self.fundingaccount) + "]"}' 

def clients_post_save(sender, instance, created, *args, **kwargs):
    if created:
        self_funding = FundingAccount.objects.get(code='SELF')
        ClientFunding.objects.create(client=instance, fundingaccount=self_funding, valid_from=timezone.now(), payment_type='cash')

post_save.connect(clients_post_save, sender=Client)


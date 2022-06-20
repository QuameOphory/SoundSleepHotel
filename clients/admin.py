from django.contrib import admin
from .models import Client, FundingAccount, ClientFunding
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    '''Admin View for Client'''

    list_display = ('client_number', 'first_name', 'middle_name', 'last_name', 'age', 'gender',)
    list_filter = ('client_number', 'funding_account',)
    search_fields = ('client_number', 'last_name', 'first_name')


@admin.register(FundingAccount)
class FundingAccountAdmin(admin.ModelAdmin):
    '''Admin View for Client'''

    list_display = ('name', 'phone', 'email', 'country', 'region', 'town', 'street',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(ClientFunding)
class ClientFundingAdmin(admin.ModelAdmin):
    '''Admin View for Client'''

    list_display = ('client', 'fundingaccount', 'valid_from', 'valid_to', 'discount',)
    list_filter = ('client', 'fundingaccount',)
    search_fields = ('fundingaccount', 'client',)
from behave import *
from selenium.webdriver.common.keys import Keys
from unittest_assertions import AssertEqual
from app.KontoOsobiste import KontoOsobiste

assert_equal = AssertEqual()

personal_data = {
    "name": "Dariusz",
    "surname": "Januszewski",
    "pesel": "79103075873"
}

@given('a personal account with promo code "{promo_code}"')
def create_personal_account(context, promo_code):
    context.account = KontoOsobiste(personal_data["name"], personal_data["surname"], personal_data["pesel"], promo_code)

@given('a personal account with the balance of {initial_balance}')
def create_personal_account(context, initial_balance):
    context.account = KontoOsobiste(personal_data["name"], personal_data["surname"], personal_data["pesel"])
    context.account.saldo = int(initial_balance)

@when('an incoming transfer of {transfer_amount} is credited')
def incoming_transfer(context, transfer_amount):
    context.account.zaksięguj_przelew_przychodzący(int(transfer_amount))

@when('an outgoing transfer of {transfer_amount} is initiated')
def outgoing_transfer(context, transfer_amount):
    context.account.przelew_wychodzący(int(transfer_amount))

@when('an outgoing transfer of {transfer_amount} is initiated with the promo code')
def outgoing_transfer_with_promo(context, transfer_amount):
    context.account = KontoOsobiste(personal_data["name"], personal_data["surname"], personal_data["pesel"], "PROM_123")
    context.account.przelew_wychodzący(int(transfer_amount))

@when('incoming transfers of {transfer1_amount} and {transfer2_amount} are credited, and an outgoing transfer of {outgoing_amount} is initiated')
def series_of_transfers(context, transfer1_amount, transfer2_amount, outgoing_amount):
    context.account.zaksięguj_przelew_przychodzący(int(transfer1_amount))
    context.account.zaksięguj_przelew_przychodzący(int(transfer2_amount))
    context.account.przelew_wychodzący(int(outgoing_amount))

@when('an express outgoing transfer of {transfer_amount} is initiated')
def express_outgoing_transfer(context, transfer_amount):
    context.account.przelew_wychodzący_ekspresowy(int(transfer_amount))

@then('the balance should be {expected_balance}')
def check_balance(context, expected_balance):
    assert_equal(context.account.saldo, int(expected_balance))

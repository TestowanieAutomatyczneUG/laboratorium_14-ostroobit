from behave import *
from src.isbn import check_isbn
from assertpy import assert_that

use_step_matcher("re")

@given("value equal to (?P<value>.+)")
def step_impl(context, value):
    context.value = value

@when("using check_valid function")
def step_impl(context):
    context.result = check_isbn(context.value)

@then("check_valid result should be (?P<result>.+)")
def step_impl(context, result):
    boo = result == "True"
    assert boo == context.result
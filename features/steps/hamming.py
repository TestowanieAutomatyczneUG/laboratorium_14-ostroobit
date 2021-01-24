from behave import *
from src.hamming import distance
from assertpy import assert_that

use_step_matcher("re")

@given("two strands")
def step_impl(context):
    context.distance = distance

@when("(?P<strand1>.+) and (?P<strand2>.+) are same length")
def step_impl(context, strand1, strand2):
    context.result = context.distance(strand1, strand2)

@then("result should be (?P<result>.+)")
def step_impl(context, result):
    assert_that(context.result).is_equal_to(int(result))
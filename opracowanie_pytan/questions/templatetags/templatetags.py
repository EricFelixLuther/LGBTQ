'''
Created on Feb 3, 2017

@author: eric
'''
from django import template

register = template.Library()

CELL_PARSE_SYMBOL = "[%TD]"
ROW_PARSE_SYMBOL = "[%TR]"

@register.filter
def format_into_list(value):
    return value.split(CELL_PARSE_SYMBOL)

@register.filter
def format_into_table(value):
    first_level = value.split(ROW_PARSE_SYMBOL)
    second_level = [string.split(CELL_PARSE_SYMBOL) for string in first_level]
    return second_level

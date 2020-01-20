# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:08:58 2019

"""

# =============================================================================
# CUSTOM EXCEPTIONS
# =============================================================================

class NotFoundError(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status
        
class BadRequest(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status
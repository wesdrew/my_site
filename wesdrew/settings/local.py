"""
Django settings for wesdrew project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!                                            
SECRET_KEY = '9#bsy!^hjd^mfo1-#jbt(8@45qjysq#xd1+wzg09=-&aaa_f-*'

# SECURITY WARNING: don't run with debug turned on in production!                                             
DEBUG = True

local_host = '127.0.0.1'
ALLOWED_HOSTS = ['testserver', local_host]




#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
@Time :    2019/11/15 15:53
@Author:  "范斯特罗夫斯基" John
@File: authentication_backends.py
@Software: PyCharm
"""
from django.contrib.auth import get_user_model


class WxBackend:
    """
    微信登陆认证
    """

    def authenticate(self, request, username=None, password=None):
        print('WxBackend, authenticate')
        print(request)
        print(username, password)
        # login_valid = (settings.ADMIN_LOGIN == username)
        login_valid = True
        # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        pwd_valid = False
        if login_valid and pwd_valid:
            try:
                user = get_user_model().objects.get(username=username)
            except get_user_model().DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = get_user_model(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        print('WxBackend, get_user')
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

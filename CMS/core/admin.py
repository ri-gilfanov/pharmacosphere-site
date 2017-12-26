from django.contrib import admin


from django.contrib.admin.sites import AdminSite


AdminSite.site_header = 'Панель управления ФармакоСфера'


from allauth import socialaccount, account
from django.contrib import auth
socialaccount.apps.SocialAccountConfig.verbose_name = 'Авторизация через сторонние сервисы'
account.apps.AccountConfig.verbose_name = 'Адреса электронной почты пользователей'
auth.apps.AuthConfig.verbose_name = 'Группы пользователей'

from django.conf.urls import url
from cuentas import views


urlpatterns = [
    # url(r'^$', views.inicio_nutri, name='nutricionista-index'),
    url(r'^login/$', views.login, name='login')
]

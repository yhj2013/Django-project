from django.conf.urls import url

from . import views


urlpatterns = [
    # 修改network表
    url(r'^networks', views.NetworkView.as_view())
]
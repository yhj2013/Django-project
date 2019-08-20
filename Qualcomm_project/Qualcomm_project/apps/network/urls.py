from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [


    # 修改network表
    url(r'^networks/$', views.NetworkView.as_view()),

    url(r'^networks/(?P<pk>\d+)/$', views.RetrieveNetworkView.as_view()),

    url(r'^networks/(?P<pk>\d+)$', views.UpdateNetworkView.as_view())
]

#
# router = DefaultRouter()
# router.register(r'^networks', views.NetworkViewSet)
#
#
# urlpatterns += router.urls
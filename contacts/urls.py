from django.conf.urls import url, include
from rest_framework import routers
from contacts import views

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet )
router.register(r'address', views.AddressViewSet)
router.register(r'group', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    ]
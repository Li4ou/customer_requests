from main import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bid/up', views.BidViewSetCreateUpdate, basename='Bid')
router.register('bid', views.BidViewSet, basename='bid')
router.register('client', views.ClientViewSet, basename='Client')
router.register('responsib', views.ResponsiblerViewSet, basename='Responsib')




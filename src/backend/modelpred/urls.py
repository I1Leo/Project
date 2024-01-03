from rest_framework import routers

from modelpred import views

router = routers.DefaultRouter()
router.register('dev', views.PredictView, basename='predict')

urlpatterns = router.urls
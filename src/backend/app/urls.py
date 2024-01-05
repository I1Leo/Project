from garpixcms.urls import *  
from django.urls import include, path
from .views import MainPageView

urlpatterns = [
  path('', MainPageView.as_view(), name='main_page'),  
  path('api/', include('modelpred.urls'))
] + urlpatterns

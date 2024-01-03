from garpixcms.urls import *  # noqa
from django.urls import include, path

urlpatterns = [
    path('api/', include('modelpred.urls'))
] + urlpatterns

from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("save",views.sv,name='save'),
    path('del',views.deleting,name='del'),
    path('update',views.updates,name='update')

]

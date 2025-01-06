
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name = 'home'),
    # path('about/',views.about),
    # path('about/<int:id>',views.about, name= 'about'),
    # path('about/page/<int:id>',views.about, name= 'about'),

    # URL e dewa sob value paite chaile.
    path('about/',views.about, name= 'about'),
]
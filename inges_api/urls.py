from django.urls import path
from inges_api.views import DirectorView,peliView, pelicula_detail_api_view, serie_detail_api_view,serieView

urlpatterns=[
    #URL DIRECTOR
    path('creacionDirector',DirectorView.as_view()), #post
    path('actualizacionDirector/<int:pkid>/', DirectorView.as_view(), name='actualizacion'), #put
    path('eliminacionDirector/<int:pkid>/', DirectorView.as_view(), name='eliminar'), #delete
    
    #URL Peli
    path('creacionPe/',peliView.as_view()), #post
    path('editarPelicula/<int:pk>/', peliView.as_view()), 
    path('eliminacionPeli/<int:pkid>/', peliView.as_view(), name='eliminacion'), #delete    
    path('peliculas/<int:pk>/', pelicula_detail_api_view.as_view(), name='pelicula_detail'),
    
    #Url Serie
    path('creacionSe/',serieView.as_view()), #post
    path('editarSerie/<int:pk>/', serieView.as_view()), #put
    path('eliminacionSe/<int:pkid>/', serieView.as_view(), name='eliminacionSe'), #delete
    path('series/<int:pk>/', serie_detail_api_view.as_view(), name='serie_detail'),
    
]
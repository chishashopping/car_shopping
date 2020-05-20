from django.urls import path

from Nearby import views


app_name = 'nearby'
urlpatterns = [
    path('citylist/',views.City.as_view(),name='citylist'),            # 城市列表
    path('aftermarket/',views.Nearby_market.as_view(),name='aftermarket'),
    path('shophome/',views.ShopHome.as_view(),name='shophome'),
]
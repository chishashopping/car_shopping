from django.urls import path

from Home import views


app_name = 'home'
urlpatterns = [
    path('banner/',views.BannerView.as_view(),name='bootpage'),      # 引导页
    path('notice/',views.NoticeView.as_view(),name='notice'),            # 公告
    path('search/',views.SearchView.as_view(),name='search'),            # 搜索
]
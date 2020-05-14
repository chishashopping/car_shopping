from django.urls import path

from Home import views


app_name = 'home'
urlpatterns = [
    path('banner/', views.BannerView.as_view(), name='banner'),                 # 引导页
    path('notice/', views.NoticeView.as_view(), name='notice'),                 # 公告
    path('search/', views.SearchView.as_view(), name='search'),                 # 搜索
    path('groupbuyList/', views.GroupBuyView.as_view(), name='groupbuy'),       # 团购列表
    path('gbProduct/', views.GbProduct.as_view(), name='gbProduct'),            # 团购商品信息
    path('gbdetail/', views.GbDetailView.as_view(), name='gbdetail'),           # 团购详情详情
    path('HomeCarshop/', views.HomeCarshopView.as_view(), name='HomeCarshop'),  # 车商城列表
    path('aftermarket/', views.MarketView.as_view(), name='market'),            # 后市场

]
from django.urls import path
from .views import homePageView, AboutPageView, contactPageView, ProductIndexView, ProductShowView, ProductCreateView, CartView, CartRemoveAllView
	
urlpatterns = [
    path("", homePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
]

'''
    path('products/product-created', ProductCreateSuccessView.as_view(), name='product-created'),
'''

from django.urls import path

from .views import ( 
	ItemDetailView, 
	checkout, 
	HomeView, 
	add_to_cart, 
	remove_from_cart,
	search, 
	search_and_show, 
	OrderSummaryView
)

app_name = 'bookstore'

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	# path('', book_list, name='home'),
	path('search/', search, name='search'),
	path('checkout/', checkout, name='checkout'), 
	path('order-summary/', OrderSummaryView.as_view(), name='order-summary'), 
	path('product-page/<slug>/', ItemDetailView.as_view(), name='product'),
	path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'), 
	path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'), 
	path('seach_results/', search_and_show, name='search_and_show_register'), 
]
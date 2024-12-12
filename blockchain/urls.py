from django.urls import path
from django.contrib import admin
from . import views
from .views import AddressDetail,ValidatorDetail,MempoolDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('create/address/', views.create_address, name='create_address'),
    path('create/validator/', views.create_validator, name='create_validator'),
    path('create/block/', views.create_block, name='create_block'),
    path('create/transaction/', views.create_transaction, name='create_transaction'),
    path('create/transaction_data/', views.create_transaction_data, name='create_transaction_data'),
    path('create/contract/', views.create_contract, name='create_contract'),
    path('create/contract_data/', views.create_contract_data, name='create_contract_data'),
    path('create/token/', views.create_token, name='create_token'),
    path('create/mempool/', views.create_mempool, name='create_mempool'),
    path('get_by/', views.get_by, name='get_by'),
    path('get_by/address/', views.get_by_address, name='get_by_address'),
    path('get_by/validator/', views.get_by_validator, name='get_by_validator'),
    path('get_by/block/', views.get_by_block, name='get_by_block'),
    path('get_by/transaction/', views.get_by_transaction, name='get_by_transaction'),
    path('get_by/transaction_data/', views.get_by_transaction_data, name='get_by_transaction_data'),
    path('get_by/contract/', views.get_by_contract, name='get_by_contract'),
    path('get_by/contract_data/', views.get_by_contract_data, name='get_by_contract_data'),
    path('get_by/token/', views.get_by_token, name='get_by_token'),
    path('get_by/mempool/', views.get_by_mempool, name='get_by_mempool'),
    path('get_all/', views.get_all, name='get_all'),
    path('get_all/address/', views.get_all_address, name='get_all_address'),
    path('get_all/validator/', views.get_all_validator, name='get_all_validator'),
    path('get_all/block/', views.get_all_block, name='get_all_block'),
    path('get_all/transaction/', views.get_all_transaction, name='get_all_transaction'),
    path('get_all/transaction_data/', views.get_all_transaction_data, name='get_all_transaction_data'),
    path('get_all/contract/', views.get_all_contract, name='get_all_contract'),
    path('get_all/contract_data/', views.get_all_contract_data, name='get_all_contract_data'),
    path('get_all/token/', views.get_all_token, name='get_all_token'),
    path('get_all/mempool/', views.get_all_mempool, name='get_all_mempool'),
    path('update/address/<str:pk>/', views.update_address, name='update_address'),
    path('delete/address/<str:pk>/', views.delete_address, name='delete_address'),

    path('update/validator/<int:pk>/', views.update_validator, name='update_validator'),
    path('delete/validator/<int:pk>/', views.delete_validator, name='delete_validator'),

    path('update/block/<str:pk>/', views.update_block, name='update_block'),
    path('delete/block/<str:pk>/', views.delete_block, name='delete_block'),

    path('update/transaction/<str:pk>/', views.update_transaction, name='update_transaction'),
    path('delete/transaction/<str:pk>/', views.delete_transaction, name='delete_transaction'),

    path('update/transaction_data/<str:pk>/', views.update_transaction_data, name='update_transaction_data'),
    path('delete/transaction_data/<str:pk>/', views.delete_transaction_data, name='delete_transaction_data'),

    path('update/contract/<str:pk>/', views.update_contract, name='update_contract'),
    path('delete/contract/<str:pk>/', views.delete_contract, name='delete_contract'),

    path('update/contract_data/<str:pk>/', views.update_contract_data, name='update_contract_data'),
    path('delete/contract_data/<str:pk>/', views.delete_contract_data, name='delete_contract_data'),

    path('update/token/<str:pk>/', views.update_token, name='update_token'),
    path('delete/token/<str:pk>/', views.delete_token, name='delete_token'),

    path('update/mempool/<str:pk>/', views.update_mempool, name='update_mempool'),
    path('delete/mempool/<str:pk>/', views.delete_mempool, name='delete_mempool'),
    path('api/address/<str:pk>/', AddressDetail.as_view(), name='address_detail'),
    path('api/address/', AddressDetail.as_view(), name='address_create'),
    path('api/address/<str:pk>/', AddressDetail.as_view(), name='address_create'),
    path('api/validator/<int:pk>/', ValidatorDetail.as_view(), name='validator_detail'),
    path('api/validator/', ValidatorDetail.as_view(), name='validator_create'),
    path('api/mempool/<str:pk>/', MempoolDetail.as_view(), name='mempool_detail'),
    path('api/mempool/', MempoolDetail.as_view(), name='mempool_create'),
    path('graphs/plotly/', views.plotly_graph, name='plotly_graph'),
    path('graphs/bokeh/', views.bokeh_graph, name='bokeh_graph'),

    # у файлі urls.py
    path('graphs/plotly/dashboard/', views.plotly_dashboard, name='plotly_dashboard'),
    path('graphs/bokeh/dashboard/', views.bokeh_dashboard, name='bokeh_dashboard'),
# Додайте ці рядки в ваш urls.py (після інших path):
path('graphs/plotly/reward_status_pie/', views.plotly_reward_status_pie, name='plotly_reward_status_pie'),
path('graphs/bokeh/reward_status_pie/', views.bokeh_reward_status_pie, name='bokeh_reward_status_pie'),

path('graphs/plotly/daily_transactions_line/', views.plotly_daily_transactions_line, name='plotly_daily_transactions_line'),
path('graphs/bokeh/daily_transactions_line/', views.bokeh_daily_transactions_line, name='bokeh_daily_transactions_line'),

path('graphs/plotly/block_scatter/', views.plotly_block_scatter, name='plotly_block_scatter'),
path('graphs/bokeh/block_scatter/', views.bokeh_block_scatter, name='bokeh_block_scatter'),

path('graphs/plotly/gas_used_histogram/', views.plotly_gas_used_histogram, name='plotly_gas_used_histogram'),
path('graphs/bokeh/gas_used_histogram/', views.bokeh_gas_used_histogram, name='bokeh_gas_used_histogram'),
    path('graphs/bokeh/interactive_difficulty/', views.bokeh_interactive_difficulty,name='bokeh_interactive_difficulty'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
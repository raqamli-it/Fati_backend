from django.urls import path
from .views import AzolarListView, Ilmiy_kengash_majlisListView, Yosh_olimlarListView, ElonlarListView

urlpatterns = [
    path('azolar/', AzolarListView.as_view(), name='azolar-list'),
    path('yosh-olimlar/', Yosh_olimlarListView.as_view(), name='yosh_olimlar-list'),
    path('ilmiy_kengash_majlis/', Ilmiy_kengash_majlisListView.as_view(), name='ilmiy_kengash_majlis-list'),
    path('elonlar/', ElonlarListView.as_view(), name='elonlar-list'),

]

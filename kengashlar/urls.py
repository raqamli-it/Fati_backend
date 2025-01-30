from django.urls import path
from kengashlar.views import (AzolarListView, Azolardetail)
from kengashlar.views import (Yosh_olimlarListView,
                              yosh_olimlardetail, ilmiy_kengash_majlisdetail, Ilmiy_kengash_majlisListView)

urlpatterns = [
    path('azolar/', AzolarListView.as_view(), name='azolar-list'),
    path('azolar/<int:pk>/', Azolardetail, name='azolar-detail'),

    path('yosh-olimlar/', Yosh_olimlarListView.as_view(), name='yosh_olimlar-list'),
    path('yosh-olimlar/<int:pk>/', yosh_olimlardetail, name='yosh_olimlar-detail'),

    path('ilmiy_kengash_majlis/', Ilmiy_kengash_majlisListView.as_view(), name='ilmiy_kengash_majlis-list'),
    path('ilmiy_kengash_majlis/<int:pk>/', ilmiy_kengash_majlisdetail, name='ilmiy_kengash_majlis'),
]
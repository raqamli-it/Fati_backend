from django.urls import path
from kengashlar.views import (AzolarListView, Azolardetail)
from kengashlar.views import (fon_pictureListView, fon_picturedetail, Yosh_olimlarListView,
                              yosh_olimlardetail, ilmiy_kengash_majlisdetail, Ilmiy_kengash_majlisListView)


urlpatterns = [
    path('azolar/', AzolarListView.as_view(), name='azolar-list'),
    path('azolar/<int:pk>/', Azolardetail, name='azolar-detail'),

    # path('DissertatsiyaIshlar/', DissertatsiyaIshlarListView.as_view(), name='DissertatsiyaIshlar-list'),
    # path('DissertatsiyaIshlar/<int:pk>/', DissertatsiyaIshlardetail, name='DissertatsiyaIshlar-detail'),

    # path('Content/', ContentListView.as_view(), name='Content-list'),
    # path('Content/<int:pk>/', Content detail, name='Content-detail'),

    path('yosh-olimlar/', Yosh_olimlarListView.as_view(), name='yosh_olimlar-list'),
    path('yosh-olimlar/<int:pk>/', yosh_olimlardetail, name='yosh_olimlar-detail'),

    path('fon_picture/', fon_pictureListView.as_view(), name='fon_picture-list'),
    path('fon_picture/<int:pk>/', fon_picturedetail, name='fon_picture-detail'),

    path('ilmiy_kengash_majlis/', Ilmiy_kengash_majlisListView.as_view(), name='ilmiy_kengash_majlis-list'),
    path('ilmiy_kengash_majlis/<int:pk>/', ilmiy_kengash_majlisdetail, name='ilmiy_kengash_majlis'),

]
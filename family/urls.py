from django.urls import path
from family import views
app_name = 'family'
urlpatterns = [
    path('', views.ParentList.as_view(), name="parents_list"),
    path('<int:pk>/', views.ParentDetail.as_view(), name="parent_detail"),
    path('<int:pk>/delete', views.ParentDelete.as_view(), name="parent_delete"),
    path('<int:pk>/edit', views.ParentUpdate.as_view(), name="parent_update"),
    path('<int:pk>/family_edit', views.FamilyUpdate.as_view(), name="family_update"),
    path('create/', views.ParentCreate.as_view(), name="parent_create"),
]
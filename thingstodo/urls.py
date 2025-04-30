from django.urls import path

from .views import (
    ThingstodoListView,
    ThingstodoDetailView,
    ThingstodoUpdateView,
    ThingstodoDeleteView,
    ThingstodoCreateView,  
)

urlpatterns = [
    path("<int:pk>/", ThingstodoDetailView.as_view(), name="thingstodo_detail"),
    path("<int:pk>/edit/", ThingstodoUpdateView.as_view(), name="thingstodo_edit"),
    path("<int:pk>/delete/", ThingstodoDeleteView.as_view(), name="thingstodo_delete"),
    path("new/", ThingstodoCreateView.as_view(), name="thingstodo_new"),
    path("", ThingstodoListView.as_view(), name="thingstodo_list"),
]

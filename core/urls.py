from django.urls import path
from django.views.generic import TemplateView


# No need for creating a view for our home page, so we used generic Template view
# To locate the html view
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'))
]

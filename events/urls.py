from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.EventListView.as_view(), name='events'),
	path('index/', views.index, name='index'),
	path('<int:pk>', views.event_detail, name='event-detail'),

]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





#Add URL maps to redirect the base URL to our application
# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='/catalog/', permanent=True)),
# ]
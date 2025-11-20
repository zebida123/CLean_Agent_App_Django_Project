from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('services/', include('services.urls')),
    path('providers/', include('providers.urls')),
    path('clients/', include('clients.urls')),
    path('bookings/', include('bookings.urls')),
    path('payments/', include('payments.urls')),
    path('wallets/', include('wallets.urls')),
    path('notifications/', include('notifications.urls')),
    path('reviews/', include('reviews.urls')),
    path('chat/', include('chat.urls')),
    path('reports/', include('reports.urls')),
]

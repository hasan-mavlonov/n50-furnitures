from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls',  namespace='pages')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('products/', include('products.urls', namespace='products')),
    path('', include('common.urls', namespace='common')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

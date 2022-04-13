from django.contrib import admin
from django.urls import path, include
from . import views  # importar el contenido del fichero views.py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),  # llama al metodo home que retorna una respuesta Http
                  path('store/', include('store.urls')),
              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)  # configuracion archivos de media para django manager

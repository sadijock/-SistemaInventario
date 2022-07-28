from django.contrib import admin
from mibodega.models import Inventario
from mibodega.models import Categoria
from mibodega.models import Usuario
# Register your models here.

# administrarlo en el panel de administrador
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Inventario)

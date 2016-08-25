from django.contrib import admin
from .models import Visit
from .models import Guest
from .models import Establishment
from .models import Contractor
from .models import Employee


admin.site.register(Visit)
admin.site.register(Guest)
admin.site.register(Establishment)
admin.site.register(Contractor)
admin.site.register(Employee)

# Register your models here.

from django.contrib import admin
from home import models                 #added
# Register your models here.
admin.site.register(models.Contact)     #added, adding this will show "Contacts" in our django admin
                                        # django admin username - admin        password - admin
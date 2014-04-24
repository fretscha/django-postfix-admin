from django.contrib import admin
from .models import Alias, Domain, Log, Mailbox, Vacation

admin.site.register(Alias)
admin.site.register(Domain)
admin.site.register(Log)
admin.site.register(Mailbox)
admin.site.register(Vacation)

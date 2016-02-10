from django.contrib import admin

from api.v0.ana.models import LottoTicket


class LottoTicketAdmin(admin.ModelAdmin):
    pass

admin.site.register(LottoTicket, LottoTicketAdmin)

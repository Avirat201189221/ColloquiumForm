from django.contrib import admin
from app.models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class PTeamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class WTBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class MovieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class SpeakerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class ClownCanardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class CodeOClockAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(PTeam,PTeamAdmin)
admin.site.register(WTB,WTBAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Speaker,SpeakerAdmin)
admin.site.register(ClownCanard,ClownCanardAdmin)
admin.site.register(CodeOClock,CodeOClockAdmin)


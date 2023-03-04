from django.contrib import admin
from app.models import PTeam
from app.models import WTB
from app.models import Movie
from app.models import Speaker
from app.models import ClownCanard
from app.models import CodeOClock
# Register your models here.
admin.site.register(PTeam)
admin.site.register(WTB)
admin.site.register(Movie)
admin.site.register(Speaker)
admin.site.register(ClownCanard)
admin.site.register(CodeOClock)
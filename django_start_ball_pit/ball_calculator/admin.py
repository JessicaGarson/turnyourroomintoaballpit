from django.contrib import admin

from ball_calculator.models import Length, Width

class LengthAdmin(admin.ModelAdmin):
    list_display = ('length_of_room',)

class WidthAdmin(admin.ModelAdmin):
    list_display = ('width_of_room',)


admin.site.register(Length, LengthAdmin)

admin.site.register(Width, WidthAdmin)
from django.contrib import admin
# Models
from portfolio.models import Language, About, Skill, Feedback, Project,  Category

# Database Config For Portfolio
class MultiDBModelAdminPortfolio(admin.ModelAdmin):
    using = 'portfolio'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

# Register Models
admin.site.register(Language, MultiDBModelAdminPortfolio)
admin.site.register(About, MultiDBModelAdminPortfolio)
admin.site.register(Skill, MultiDBModelAdminPortfolio)
admin.site.register(Feedback, MultiDBModelAdminPortfolio)
admin.site.register(Project, MultiDBModelAdminPortfolio)
admin.site.register(Category, MultiDBModelAdminPortfolio)

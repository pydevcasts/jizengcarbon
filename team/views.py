

from team.models import Member, Team
from django.views.generic import ListView


class TeamView(ListView):
    model = Team
    context_object_name = "teams"
    template_name = 'frontend/team/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members']= Member.objects.select_related('team').filter(status = 1).order_by('published_at')
        context['teams'] = Team.objects.filter(status = 1).order_by('published_at')
        context['segment'] = "Team"
        return context



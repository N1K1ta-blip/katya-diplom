from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from main.models import Work


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        context = {}
        works = Work.objects.all()[:3]
        context['works'] = works
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)


class PortfolioView(View):
    template_name = 'portfolio.html'

    def get_context(self):
        context = {}
        works = Work.objects.all()
        context['works'] = works
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)


class WorkDetailView(View):
    template_name = 'detail_portfolio.html'

    def get(self, request, *args, **kwargs): 
        work = get_object_or_404(Work, pk=kwargs['pk'])
        context = {'work': work}
        return render(request, self.template_name, context)


class AboutUsView(View):
    template_name = 'aboutUS.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

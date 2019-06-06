from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Job


class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/home.html'
    paginate_by = 20

    def get_queryset(self):
        p = super().get_queryset()
        q = self.request.GET.get('search')
        if q is not None:
            p = p.filter(title__icontains=q)
        return p

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context
    # def get_queryset(self):
    #     queryset = Job.objects.all().order_by('-job_number')
    #     return queryset


# def home(request):
#     queryset = Job.objects.all().order_by('-job_number')
#     page = request.GET.get('page', 1)
#     paginator = Paginator(queryset, 20)

#     try:
#         jobs = paginator.page(page)
#     except PageNotAnInteger:
#         # fallback to the first page
#         jobs = paginator.page(1)
#     except EmptyPage:
#         # probably the user tried to add a page number
#         # in the url, so we fallback to the last page
#         jobs = paginator.page(paginator.num_pages)
#     return render(request, 'jobs/home.html', {'jobs': jobs})


def job_detail(request, pk, slug):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

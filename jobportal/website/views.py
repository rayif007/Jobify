from django.shortcuts import render
from job.models import Job, ApplyJob
from .filter import Jobfilter


def home(request):
    filter = Jobfilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    context = {'filter': filter}
    return render(request, 'website/home.html', context)


def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs': jobs}
    return render(request, 'website/job_listing.html', context)


def job_details(request, pk):
    job = Job.objects.get(pk=pk)
    if request.user.is_authenticated:
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            has_applied = True
        else:
            has_applied = False
        # job = Job.objects.get(pk=pk)
        context = {'job': job, 'has_applied': has_applied}
        return render(request, 'website/job_details.html', context)
    else:
        context = {'job': job, }
        return render(request, 'website/job_details.html', context)

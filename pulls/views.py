# Django
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from rest_framework import viewsets

# Models and Serializers
from .models import PR
from .serializers import PRSerializer, CreatePRSerializer


def pull_update(request, pk):
    pull = get_object_or_404(PR, pk=pk)
    pull.status = 'CLOSED'
    pull.save()
    messages.success(request, 'Status was changed to CLOSED')
    return render(request, 'branches/pulls.html', {"pulls": PR.objects.all()})


class PRViewSet(viewsets.ModelViewSet):
    queryset = PR.objects.all()
    serializer_class = PRSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePRSerializer
        return PRSerializer

    def change_status(request, pk):
        pull = get_object_or_404(PR, pk=request.GET.get('pull_id'))
        pull.status = not pull.status
        pull.save()
        return redirect('branches/pulls.html')


"""
    ############THIS FUNCTIONS DO NOT WORKS#####
    def merge(request):
        if request.method == 'POST':
            form = PullCreateView(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('pull-create')




    def get_messages(request):
        messages.info(request, 'Merge was succesfully')
        messages.success(request, 'Profile details updated.')
        messages.warning(request, 'Your account expires in three days.')
        return getattr(request, '_messages', [])
        
    #Testing function it doesn't work yet
    def change_status(request, pk):
        if request.GET.get('closed'):
            pull = get_object_or_404(PR, pk=pk)
            pull.status = 'OPEN' if pull.status == 'CLOSED' else 'CLOSED'
            pull.save(update_fields=['is_published'])
            messages.success(request, 'Test number {} {} successfully'.format(pk, pull.status))
            return redirect('branches/pulls.html')
"""

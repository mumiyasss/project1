from django.shortcuts import render
from .models import polls
from .forms import checkForm

# Create your views here.
def show_all_polls(request):
    listOfAllPolls = polls.objects.all()
    return render(request, 'polls/voting.html', {'allPolls': listOfAllPolls })

def poll_vote(request, poll_id):
    poll = polls.objects.get(poll_id)
    return render(request, 'polls/voting_detail.html', {'poll': poll})

def get_vote(request, poll_id):
    if request.method == 'POST':
        form = checkForm(request.POST)

        if form.is_valid():
            pass

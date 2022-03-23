from pydoc_data.topics import topics
from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """Learning Log app homepage"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Shows topics list"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
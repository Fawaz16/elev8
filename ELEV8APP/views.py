import imp
from pydoc_data.topics import topics
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from .models import Topic
from .models import content_post
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    '''render the home page'''
    my_topics=Topic.objects.all()
    # new_topic=Header.objects.all()
    return render(request,'index.html', {'topics': my_topics})
    
@login_required
def content(request,post_id):
    '''render the content page'''
    print(post_id)
    topic=Topic.objects.get(id=post_id)
    headlines=content_post.objects.all()[0]
    print(headlines)
    if request.method == 'POST':
        comment= Comment()
        comment.post =topic
        comment.owner=request.user
        comment.body = request.POST.get('user_comment')
        comment.save()
    comments =topic.comment_set.all()
    return render(request, 'content.html', {'topic': topic,'new_topic': headlines,'comments':comments})


    


def edit(request):
    '''render edit page'''
    return render(request, 'edit.html')

def email(request):
    '''render email page'''
    return render(request,'email.html')

def profile(request):
    '''render profile page'''
    return render(request,'profile.html')

def edit_task(request):
    '''display user email'''
    user_input=request.GET.get('task_to_edit')
    print(user_input)
    return redirect('home')


def signup(request):
    '''render signup page'''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= UserCreationForm()

    return render(request, 'sign.html', {'form': form})

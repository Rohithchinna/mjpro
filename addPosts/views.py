from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import CreateView,ListView
from django.views import View
from django.urls import reverse_lazy
from .models import myPosts,likes
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from profiles.models import profiles

# Create your views here.
@login_required
def addPosts(request):
    filters=myPosts.objects.filter(profile=profiles.objects.get(user_name=request.user)).order_by("-posted_at")

    return render(request,"addPosts.html",{'posts':filters})

@method_decorator(login_required, name='dispatch')  # Apply the decorator to the dispatch method
class UploadPost(CreateView,ListView):
    model=myPosts
    success_url=reverse_lazy('addPosts')
    context_object_name='posts'
    def get_queryset(self):

        return myPosts.objects.filter(profile=self.request.user)
    def post(self, request, *args, **kwargs):
        profile=profiles.objects.get(user_name=request.user)
        post=None
        resource=None
        if('file' in self.request.FILES):
            print("hi")
            post=request.FILES.get('file')
        title=request.POST.get('title')
        description=request.POST.get('description')
        if(request.POST.get('resource')):
            resource=request.POST.get('resource')
        myPostsInst=myPosts(profile=profile,title=title,description=description,post=post,resource=resource)
        myPostsInst.save()
        return redirect(self.success_url)

@login_required
def addLike(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        liked_by = request.POST.get('liked_by')
        print(post_id,liked_by)
        # Get the post and the user profile
        post = myPosts.objects.get(id=post_id)
        liked_by = profiles.objects.get(user_name=request.user)

        # Create a new like
        like,created = likes.objects.get_or_create(post=post)
        like.liked_by.add(liked_by)
        like.likes+=1
        like.save()

        # Return a JSON response
        return JsonResponse({'status': 'success', 'message': 'Post liked successfully!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
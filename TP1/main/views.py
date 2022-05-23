from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
#from matplotlib.style import context
from .forms import RegisterForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Post, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView

@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
    
    search = request.GET.get('search', '')
    posts_search = posts.filter(Q(title__icontains = search) | Q(description__icontains = search))

    return render(request, 'main/home.html', {"posts": posts_search})


@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'main/thread.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        ph = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = ph.total_likes()
        context['total_likes']=  total_likes
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main/create_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)



def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #user = request.user
    #if user in post.likes.all():
    #    post.likes.remove(user)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('thread', args=[str(pk)]))
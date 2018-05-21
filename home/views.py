from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.forms import HomeForm
from home.models import Post, Friend


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        # friend = Friend.objects.get(current_user=request.user)
        # friends = friend.users.all()

        context = {'form': form, 'posts': posts, 'users': users}
                   # 'friends': friends}
        return render(request, self.template_name, context)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            # return redirect('home:home')

        context = {'form': form, 'text': text}
        return render(request, self.template_name, context)

# I don't Understand
def change_friends(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, new_friend)

    return redirect('home:home')






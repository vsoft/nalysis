from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articles, Comment
from .forms import CommentForm

class IndexView(generic.ListView):
    template_name = 'sports/index.html'
    context_object_name = 'all_articles'

    def get_queryset(self):
        return Articles.objects.all()

class DetailsView(generic.DetailView):
    model = Articles
    template_name = 'sports/detail.html'
    form = CommentForm()

    def get(self, request, pk):
        article = Articles.objects.get(pk=pk)
        comments = Comment.objects.all()
        return render(request, self.template_name, {'form': self.form, 'article': article, 'comments': comments})

    def post(self, request, pk):
        article = Articles.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['content']
            post = Comment(article=article, person=name, message=comment)
            post.save()
            form = CommentForm()
            comments = Comment.objects.all()
            return render(request, self.template_name, {'form': form, 'article': article, 'comments': comments})
        return render(request, self.template_name, {'form': self.form, 'article': article})

class CreateComment(CreateView):
    model = Comment
    fields = ['Name', 'Message']

class NFLView(generic.ListView):
    template_name = 'sports/nfl.html'
    context_object_name = 'all_articles'

    def get_queryset(self):
        return Articles.objects.all().filter(category='NFL')

class NBAView(generic.ListView):
    template_name = 'sports/nba.html'
    context_object_name = 'all_articles'

    def get_queryset(self):
        return Articles.objects.all().filter(category='NBA')

class AboutView(generic.ListView):
    template_name = 'sports/about.html'

    def get_queryset(self):
        return Articles.objects.all()
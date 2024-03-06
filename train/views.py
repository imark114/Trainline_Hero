from django.shortcuts import render
from .models import Train,SourceStation, DestinationStation
from django.views.generic import TemplateView, DetailView
from booking.forms import CommentForm
# Create your views here.


def TrainView(request):
    trains = Train.objects.all()
    return render(request,'train_view.html', {'trains': trains})


def FilterTrain(request):
    trains = Train.objects.all()
    source = SourceStation.objects.all()
    destination = DestinationStation.objects.all()
    if request.method == "GET":
        slct_src = request.GET.get('source')
        slct_dst = request.GET.get('destination')
        trains = Train.objects.filter(source_station=slct_src, destination_station=slct_dst)
    return render(request,'filter_train.html', {'trains': trains, 'source': source, 'destination': destination})

class TrainDetailsView(DetailView):
    model = Train
    template_name = 'train_details.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        train = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.train = train
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        train = self.get_object()
        comments = train.comments.all()
        context['comments'] = comments
        comment_form = CommentForm
        context['comment_form'] = comment_form
        context["type"] = 'Train Details'
        return context


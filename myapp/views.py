from django.shortcuts import render,redirect,get_object_or_404
from .models import Ad
from .forms import AdForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    ads = Ad.objects.all()
    return render(request,'index.html',{'ads':ads})


@login_required 
def sell_toy(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.seller = request.user
            ad.save()
            return redirect('ad_detail', ad_id=ad.pk)
    else:
        form = AdForm()
    return render(request, 'sell_toy.html', {'form': form})

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ad_details.html', {'ad': ad})

@login_required
def user_ads(request):
    ads = Ad.objects.filter(seller=request.user)
    return render(request, 'user_ads.html', {'ads': ads})
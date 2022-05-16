from django.shortcuts import render
from django.http import HttpResponse

k_popGroup = [
    {
        'groupName': 'BLACKPINK',
        'debut_date': '08/08/2016',
        'description': 'BLACKPINK (블랙핑크) consists of 4 members: Jisoo, Jennie, Rosé, and Lisa. The band debuted on August 8th, 2016 under YG Entertainment. On October 23, 2018, BLACKPINK has officially signed with the U.S. label Interscope Records.',
        'fandom_name': '',
        'total_albums': '',
        'total_members': '',
        'members_name': '',
    }
]

# Create your views here.
def home(request):
    return render(request, 'kphoco/kphoco.html') #Still returning HTTP Response


def about(request):
    return render(request, 'kphoco/about.html')
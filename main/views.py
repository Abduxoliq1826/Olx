from datetime import date
from tkinter.messagebox import QUESTION
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    d1 = date.today()
    month = Ads.objects.filter(date__month=d1.month)
    context = {
        'month': month,
        'user': request.user,
        'ads': Ads.objects.all().count(),
        'is_admin': Ads.objects.filter(status=1).count(),
        'reject': Ads.objects.filter(status=3).count(),
        'assept': Ads.objects.filter(status=2).count(),
        'sold': Ads.objects.filter(status=4).count(),

    }
    print(month)
    return render(request, 'dashboard.html', context)

def Login(request):
    return render(request, 'login.html',)

def DistircView(request):
    a = Distirc.objects.all()
    context = {
        'a' : a
    }
    return render(request, 'distirc.html', context)


def District_create(request):
    name = request.POST.get('name')
    a = Distirc.objects.create(name=name)
    return redirect('distirc')


def District_delete(request, pk):
    a = Distirc.objects.get(id=pk)
    a.delete()
    return redirect('distirc')

def District_update(request, pk):
    if request.method=='GET':
        context = {
            'a' : Distirc.objects.get(id=pk)
        }
        return render(request, 'distirc_single.html', context)
    if request.method=='POST':
        name = request.POST.get('name')
        a = Distirc.objects.get(id=pk)
        a.name = name
        a.save()
        context = {
            'a' : Distirc.objects.get(id=pk)
        }
        return render(request, 'distirc_single.html', context)
        
    

def Distirc_all(request):
    a = Distirc.objects.all()
    data = {
        'a' : a
    }    
    return render(request, 'distirc.html', data)



@login_required(login_url='login')
def ProductFilter(request):
    a = Ads.objects.filter(status=1)
    context = {
        'is_admin': a,
        'user': request.user,
    }
    return render(request, 'is_admin.html', context)


@login_required(login_url='login')
def About(request, pk):
    a = Ads.objects.get(id=pk)
    context = {
        'about': a,
        'user': request.user,
    }
    return render(request, 'about.html', context)


def Logins(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user1 = User.objects.filter(username=username)
    if user1 is not None:
        user = User.objects.get(username=username)
        usr = authenticate(username=username, password=password)
        if user.type == 1:
            if usr is not None:
                login(request, usr)
                return redirect('dashboard')
            else:
                return redirect('login')
        else:
            return redirect('login')
    return redirect('login')


def LogOut(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def All_User(request):
    context = {
        'user': User.objects.filter(type=2),

    }
    return render(request, 'users.html', context)


@login_required(login_url=login)
def AllAds(request):
    ads = Ads.objects.all()
    context = {
        'ads': ads,
    }
    return render(request, 'ads.html', context)



@login_required(login_url='login')
def IsAcepted(request):
    a = Ads.objects.filter(status=2)
    context = {
        'ads': a
    }
    return render(request, 'is_acepted.html', context)


@login_required(login_url='login')
def IsRejected(request):
    a = Ads.objects.filter(status=3)
    context = {
        'ads' : a
    }
    return render(request, 'is_rejected.html', context)


@login_required(login_url=login)
def Sold(request):
    a = Ads.objects.filter(status=4)
    context = {
        'ads' : a
    }
    return render(request, 'sort.html', context)


@login_required(login_url=login)
def Users(request,pk):
    context = {
        'ads': Ads.objects.filter(owner_id=pk),

    }
    return render(request, 'users2.html', context)

@login_required(login_url='login')
def InformationViews(request):
    if request.method == 'GET':
        context = {
            'info': Information.objects.last(),
        }
        return render(request, 'info.html', context)
    elif request.method == 'POST':
        company_name = request.POST.get('company_name')
        logo = request.FILES.get('logo')
        description = request.POST.get('description')
        googleplay = request.POST.get('googleplay')
        appstore = request.POST.get('appstore')
        if company_name == "" and description == "" and googleplay == "" and appstore == "" and logo == "":
            context = {
                'info': Information.objects.last(),
            }
            return render(request, 'info.html', context)
        else:
            Information.objects.create(company_name=company_name, logo=logo, description=description,
                                       googleplay=googleplay, appstore=appstore,
                                       )
            context = {
                'info': Information.objects.last(),
            }
            return render(request, 'info.html', context)


@login_required(login_url=login)
def DeleteInfo(request, pk):
    info = Information.objects.get(id=pk)
    info.delete()
    return redirect('infos')


@login_required(login_url=login)
def InformationsViews(request):
    context = {
        'info': Information.objects.all()
    }
    return render(request, 'infos.html', context)


@login_required(login_url='login')
def Accepted(request, pk):
    ads = Ads.objects.get(id=pk)
    ads.status = 2
    ads.save()
    return redirect('productfilter')


@login_required(login_url='login')
def Rejected(request, pk):
    ads = Ads.objects.get(id=pk)
    ads.status = 3
    ads.save()

    return redirect('productfilter')


@login_required(login_url='login')
def AdsSingle(request, pk):

    context = {
        'ads': Ads.objects.get(id=pk)
    }
    return render(request, 'single-ads.html', context)


@login_required(login_url=login)
def UpdateUser(request):
    user = request.user
    if user is not None:
        if request.method == "POST":
            username = request.POST.get('username')
            image = request.FILES.get('image')
            last_password = request.POST.get('last_password')
            new_password = request.POST.get('new_password')
            restartpassword = request.POST.get('restartpassword')
            usr = authenticate(username=user.username, password=last_password)
            if new_password == restartpassword:
                if usr is not None:
                    usr.username = username
                    usr.image = image
                    usr.set_password(restartpassword)
                    usr.save()
                    return redirect('dashboard')
                return redirect('reset')
            return redirect('reset')
        return redirect('users')
    return redirect('login')


@login_required(login_url='login')
def Reset(request):
    user = request.user
    users = User.objects.get(id=user.id)
    context = {
        'user': user
    }
    return render(request, 'updateuser.html', context)


@login_required(login_url=login)
def AddCategory(request):
    if request.method == 'GET':
        context = {
            'category': Category.objects.all()
        }
        return render(request, 'category.html', context)
    name = request.POST.get('name')
    photo = request.FILES.get('photo')
    if name=="" and photo=="":
        Category.objects.create(name=name, photo=photo)
        context = {
            'category': Category.objects.all()
        }
        return render(request, 'category.html', context)
    else:
        context = {
            'category': Category.objects.all()
        }
        return render(request, 'category.html', context)


@login_required(login_url=login)
def Regions(request):
    if request.method == 'GET':
        context = {
            'region': Region.objects.all(),
            'distric': Distirc.objects.all(),
        }
        return render(request, 'region.html', context)
    elif request.method == 'POST':
        category = request.POST.getlist('category')
        name = request.POST.get('name')
        if category == [] and name == "" :
            context = {
                'region': Region.objects.all(),
                'distric': Distirc.objects.all()
            }
            return render(request, 'region.html', context)
        else:
            region = Region.objects.create(name=name)
            for i in category:
                region.distirc.add(Distirc.objects.get(id=i))
            region.save()
            context = {
                'region': Region.objects.all(),
                'distric': Distirc.objects.all()
            }
            return render(request, 'region.html', context)


@login_required(login_url=login)
def SubCategory(request):
    if request.method == 'GET':
        context = {
            'subcategory': Subcategory.objects.all(),
            'category': Category.objects.all()
        }
        return render(request, 'subcategory.html', context)
    elif request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        if name == "" and category == "":
            context = {
                'subcategory': Subcategory.objects.all()
            }
            return render(request, 'subcategory.html', context)
        else:
            Subcategory.objects.create(name = name, category_id = category)
            context = {
                'subcategory': Subcategory.objects.all()
            }
            return render(request, 'subcategory.html', context)


@login_required(login_url=login)
def SingleCategory(request,pk):
    if request.method == 'GET':
        context = {
            'category': Category.objects.get(id=pk),
        }
        return render(request, 'singlecategory.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES.get('photo')
        if name=="" and photo=="":
            context = {
                'category': Category.object.get(id=pk),
            }
            return render(request, 'singlecategory.html', context)
        else:
            category = Category.objects.get(id=pk)
            category.name = name
            category.photo = photo
            category.save()
            context = {
                'category': category,
            }
            return render(request, 'singlecategory.html', context)


@login_required(login_url=login)
def DeleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category')


@login_required(login_url=login)
def SingleSubCategory(request,pk):
    if request.method == 'GET':
        context = {
            'subcategory': Subcategory.objects.get(id=pk),
            'category': Category.objects.all(),
        }
        return render(request, 'singlesubcategory.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        if name=="" and category=="":
            subcategory = Subcategory.objects.get(id=pk)
            context = {
                'subcategory': subcategory,
                'category': Category.objects.all(),
            }
            return render(request, 'singlesubcategory.html', context)
        else:
            subcategory = Subcategory.objects.get(id=pk)
            subcategory.name = name
            subcategory.category_id = category
            subcategory.save()
            context = {
                'subcategory': subcategory,
                'category': Category.objects.all(),
            }
            return render(request, 'singlesubcategory.html', context)


@login_required(login_url=login)
def DeleteSubCategory(request, pk):
    subcategory = Subcategory.objects.get(id=pk)
    subcategory.delete()
    return redirect('subcategory')


@login_required(login_url=login)
def SingleRegion(request,pk):
    if request.method == 'GET':
        context = {
            'region': Region.objects.get(id=pk),
            'user':request.user,
            'distric': Distirc.objects.all(),
        }
        return render(request, 'single-region.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        distric = request.POST.getlist('dictric')
        if name=="" and distric==[]:
            region = Region.objects.get(id=pk)
            context = {
                'region': region,
                'distric': Distirc.objects.all(),
            }
            return render(request, 'single-region.html', context)
        else:
            region = Region.objects.get(id=pk)
            region.name = name
            for i in distric:
                region.distirc.add(Distirc.objects.get(id=i))
            region.save()
            context = {
                'region': region,
                'distric': Distirc.objects.all(),
            }
            return render(request, 'single-region.html', context)



@login_required(login_url=login)
def DeleteRegion(request, pk):
    region = Region.objects.get(id=pk)
    region.delete()
    return redirect('regions')



@login_required(login_url=login)
def Help_q_Create(request):
    if request.method=='POST':
        question = request.POST.get('question')
        if question == "":
            context = {
                'question': Helps_q.objects.all().order_by('-id')
            }
            return render(request, 'helps_q.html', context)
        else:
            Helps_q.objects.create(question=question)
            context = {
                'question' : Helps_q.objects.all().order_by('-id')
            }
            return render(request, 'helps_q.html', context)

def Delete_hq(request, pk):
    Helps_q.objects.get(id=pk).delete()
    return redirect('helps_q')

def Update_hq(request, pk):
    if request.method=='GET':
        context = {
            'info': Helps_q.objects.get(id=pk),
        }
        return render(request, 'single_hq.html', context)
    elif request.method == 'POST':
        question = request.POST.get('question')
        if question == "":
            context = {
                'info': Helps_q.objects.get(id=pk),
            }
            return render(request, 'single_hq.html', context)
        else:
            hq = Helps_q.objects.get(id=pk)
            hq.question=question
            hq.save()
            context = {
                'info': Helps_q.objects.get(id=pk),
            }
            return render(request, 'single_hq.html', context)




@login_required(login_url=login)
def Help_a_Create(request):
    if request.method=='GET':
        context = {
            'answer': Helps_a.objects.all().order_by('-id'),
            'question': Helps_q.objects.all().order_by('-id'),
        }
        return render(request, 'helps_a.html', context)
    elif request.method=='POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        if question=="" and answer=="":
            context = {
                'answer': Helps_a.objects.all().order_by('-id'),
                'question': Helps_q.objects.all().order_by('-id'),
            }
            return render(request, 'helps_a.html', context)
        else:
            Helps_a.objects.create(answer=answer, question_id=question)
            context = {
                'answer' : Helps_a.objects.all().order_by('-id'),
                'question' : Helps_q.objects.all().order_by('-id'),
            }
            return render(request, 'helps_a.html', context)


def Delete_ha(request, pk):
    Helps_a.objects.get(id=pk).delete()
    return redirect('helps_a')


def Update_ha(request, pk):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        if question=="" and answer=="":
            context = {
                'info': Helps_a.objects.get(id=pk),
                'question': Helps_q.objects.all().order_by('-id'),
            }
            return render(request, 'single_ha.html', context)
        else:
            ha = Helps_a.objects.get(id=pk)
            ha.question_id=question
            ha.answer=answer
            ha.save()
            context = {
                'info' : Helps_a.objects.get(id=pk),
                'question' : Helps_q.objects.all().order_by('-id'),
            }
            return render(request, 'single_ha.html', context)

def handler404(request, *args, **argv):
    return render(request, 'pages-404.html')
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View
from . forms import *
from . models import *
from .models import Image

from .forms import ImageForm

from django.db.models import Q
# Create your views here.

def home(request):
    book = Book.objects.all()
    image = Image.objects.all()
    user = User.objects.all()
    context = {
        'book': book,
        'image': image,
        'user': user
    }
    return render(request, 'corr/home.html')

class userReservationList(View):
    def get(self, request):
        if 'SearchUser' in request.GET:
            q1 = request.GET['q1']
            q2 = request.GET['q2']
            q3 = request.GET['q3']
            print(q3)
            # multiQ = Q(Q(employee_id__icontains=q) & Q(firstname__icontains=q) )

            if q1 and q2 != '':
                user = User.objects.filter(udate=q1).filter(
                    Q(ufirstname=q2) | Q(ulastname=q2))
                image = Image.objects.all()
                #designation = Designation.objects.all()

            elif q1 and q3 != '':
                user = User.objects.filter(
                    udate=q1).filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()

            elif q2 and q3 != '':
                user = User.objects.filter(Q(Q(ufirstname=q2) | Q(
                    ulastname=q2))).filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()

            else:
                if q3 == '':
                    user = User.objects.filter(Q(Q(
                        ufirstname=q2) | Q(ulastname=q2))) or User.objects.filter(Q(udate=q1))
                else:
                    user = User.objects.filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()
            # print(employee)
            # department = Department.objects.all()
            # designation = Designation.objects.all()
        else:
            image = Image.objects.all()
            #designation = Designation.objects.all()
            user = User.objects.all()

        context = {
            'image': image,
            'user': user,
        }

        return render(request, 'corr/userReservationList.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                did=request.POST.get("user-Id")
                date=request.POST.get("u-udate")
                startTime=request.POST.get("u-ustartTime")
                endTime=request.POST.get("u-uendTime")
                title=request.POST.get("i-title")
                prefix=request.POST.get("u-uprefix")
                firstname=request.POST.get("u-ufirstname")
                middlename=request.POST.get("u-umiddlename")
                lastname=request.POST.get("u-ulastname")

                update_book = Book.objects.filter(id=did).update(udate=date, ustartTime=startTime, 
                uendTime=endTime, title=title, uprefix=prefix, ufirstname=firstname, umiddlename=middlename, ulastname=lastname)
                print(update_book)

                print('profile updated')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                did=request.POST.get("uuser-id")
                book=Book.objects.filter(id=did).delete()
                print('recorded deleted')

        return redirect('user_list')

class latestReservation(View):   
    def get(self, request):
        if 'SearchBook' in request.GET:
            q1 = request.GET['q1']
            q2 = request.GET['q2']
            q3 = request.GET['q3']
            print(q3)
            # multiQ = Q(Q(employee_id__icontains=q) & Q(firstname__icontains=q) )

            if q1 and q2 != '':
                book = Book.objects.filter(date=q1).filter(
                    Q(firstname=q2) | Q(lastname=q2))
                image = Image.objects.all()
                #designation = Designation.objects.all()

            elif q1 and q3 != '':
                book = Book.objects.filter(
                    date=q1).filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()

            elif q2 and q3 != '':
                book = Book.objects.filter(Q(Q(firstname=q2) | Q(
                    lastname=q2))).filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()

            else:
                if q3 == '':
                    book = Book.objects.filter(Q(Q(
                        firstname=q2) | Q(lastname=q2))) or Book.objects.filter(Q(date=q1))
                else:
                    book = Book.objects.filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()
            # print(employee)
            # department = Department.objects.all()
            # designation = Designation.objects.all()
        else:
            image = Image.objects.all()
            #designation = Designation.objects.all()
            book = Book.objects.all()

        context = {
            'image': image,
            'book': book,
        }

        return render(request, 'corr/latestReservation.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                did=request.POST.get("book-Id")
                date=request.POST.get("d-date")
                startTime=request.POST.get("d-startTime")
                endTime=request.POST.get("d-endTime")
                title=request.POST.get("i-title")
                prefix=request.POST.get("d-prefix")
                firstname=request.POST.get("d-firstname")
                middlename=request.POST.get("d-middlename")
                lastname=request.POST.get("d-lastname")

                update_book = Book.objects.filter(id=did).update(date=date, startTime=startTime, 
                endTime=endTime, title=title, prefix=prefix, firstname=firstname, middlename=middlename, lastname=lastname)
                print(update_book)

                print('profile updated')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                did=request.POST.get("bbook-id")
                book=Book.objects.filter(id=did).delete()
                print('recorded deleted')

        return redirect('latest_reservation')

def create(request):
    return render(request, 'corr/create.html')

class vacant(View):
    def get(self, request):
        book = Book.objects.all()
        image = Image.objects.all()
        context ={
            'book': book,
            'image': image
        }

        titles_to_exclude = [book.title for book in Book.objects.all()]
        Image.objects.exclude(title__in=titles_to_exclude)
        
        return render(request, 'corr/vacant.html', context)
    
    def post(self, request):
        

        return redirect('vacantRoom')

class roomList(View):
    def get(self, request):
        if 'SearchRoom' in request.GET:
            q1 = request.GET['q1']
            q2 = request.GET['q2']
            q3 = request.GET['q3']
            print(q3)
            # multiQ = Q(Q(employee_id__icontains=q) & Q(firstname__icontains=q) )

            if q1 and q2 != '':
                book = Book.objects.filter(date=q1).filter(
                    Q(firstname=q2) | Q(lastname=q2))
                image = Image.objects.all()
                #designation = Designation.objects.all()

            elif q1 and q3 != '':
                book = Book.objects.filter(
                    date=q1).filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()

            elif q2 and q3 != '':
                book = Book.objects.filter(Q(Q(firstname=q2) | Q(
                    lastname=q2))).filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()

            else:
                if q3 == '':
                    book = Book.objects.filter(Q(Q(
                        firstname=q2) | Q(lastname=q2))) or Book.objects.filter(Q(date=q1))
                else:
                    book = Book.objects.filter(title=q3)
                image = Image.objects.all()
                #designation = Designation.objects.all()
            # print(employee)
            # department = Department.objects.all()
            # designation = Designation.objects.all()
        else:
            image = Image.objects.all()
            #designation = Designation.objects.all()
            book = Book.objects.all()

        context = {
            'image': image,
            'book': book
        }
        return render(request, 'corr/roomList.html', context)
 #   def get(self, request):
  #      image = Image.objects.all()
   #     return render(request, 'corr/roomList.html',{'image': image})

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                iid=request.POST.get("room-Id")
                title=request.POST.get("i-title")
                image=request.POST.get("i-image")
                details=request.POST.get("i-details")
                price=request.POST.get("i-price")

                update_image = Image.objects.filter(id=iid).update(title=title, details=details, price=price)
                print(update_image)

                print('profile updated')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                iid=request.POST.get("rroom-id")
                image=Image.objects.filter(id=iid).delete()
                print('recorded deleted')

        return redirect('room_list')

class res(View):
    def get(self, request):
        book = Book.objects.all()
        image = Image.objects.all()
        context ={
            'book': book,
            'image': image
        }
        return render(request, 'corr/res.html', context)
    
    def post(self, request):
        form = BookForm(request.POST)
        date = request.POST.get("date")
        print(date)
        startTime = request.POST.get("startTime")
        print(startTime)
        endTime = request.POST.get("endTime")
        print(endTime)
        title = request.POST.get("title")
        print(title)
        prefix = request.POST.get("prefix")
        print(prefix)
        firstname = request.POST.get("firstname")
        print(firstname)
        middlename = request.POST.get("middlename")
        print(middlename)
        lastname = request.POST.get("lastname")
        print(lastname)
        gender = request.POST.get("gender")
        print(gender)
        age = request.POST.get("age")
        print(age)
        address = request.POST.get("address")
        print(address)
        email = request.POST.get("email")
        print(email)
        number = request.POST.get("number")
        print(number)

        if form.is_valid():
            date = request.POST.get("date")
            startTime = request.POST.get("startTime")
            endTime = request.POST.get("endTime")
            title = request.POST.get("title")
            prefix = request.POST.get("prefix")
            firstname = request.POST.get("firstname")
            middlename = request.POST.get("middlename")
            lastname = request.POST.get("lastname")
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            address = request.POST.get("address")
            email = request.POST.get("email")
            number = request.POST.get("number")
        
        form = Book(date = date, startTime=startTime, endTime=endTime, title_id=title, prefix = prefix, 
                    firstname=firstname, middlename=middlename, lastname=lastname, gender = gender, 
                    age = age, address = address, email = email, number = number)
        form.save()

        return redirect('latest_reservation')

class res1(View):
    
    def get(self, request):
        return render(request, 'corr/res1.html')
    
    def post(self, request):
        form = ContinueForm(request.POST)
        gender = request.POST.get("gender")
        print(gender)
        age = request.POST.get("age")
        print(age)
        address = request.POST.get("address")
        print(address)
        email = request.POST.get("email")
        print(email)
        number = request.POST.get("number")
        print(number)

        if form.is_valid():
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            address = request.POST.get("address")
            email = request.POST.get("email")
            number = request.POST.get("number")
        
        form = Continue(gender = gender, age=age, address=address, email=email, number = number)
        form.save()

        return redirect('latest_reservation')

def upload(request):
    return render(request, 'corr/upload.html')

def rooms(request):
    return render(request, 'corr/rooms.html')

def dashboard(request):
    return render(request, 'corr/dashboard.html')

def signin(request):
    return render(request, 'corr/signin.html')

def index(request):
    return render(request, 'corr/index.html')

class reservation(View):
    def get(self, request):
        book = Book.objects.all()
        image = Image.objects.all()
        user = User.objects.all()
        context = {
            'book': book,
            'image': image,
            'user': user
        }
        return render(request, 'corr/reservation.html', context)
    
    def post(self, request):
        form = UserForm(request.POST)
        udate = request.POST.get("udate")
        print(udate)
        ustartTime = request.POST.get("ustartTime")
        print(ustartTime)
        uendTime = request.POST.get("uendTime")
        print(uendTime)
        title = request.POST.get("title")
        print(title)
        uprefix = request.POST.get("uprefix")
        print(uprefix)
        ufirstname = request.POST.get("ufirstname")
        print(ufirstname)
        umiddlename = request.POST.get("umiddlename")
        print(umiddlename)
        ulastname = request.POST.get("ulastname")
        print(ulastname)
        uage = request.POST.get('uage')
        print(uage)
        ugender = request.POST.get("ugender")
        print(ugender)
        uaddress = request.POST.get("uaddress")
        print(uaddress)
        uemail = request.POST.get("uemail")
        print(uemail)
        unumber = request.POST.get("unumber")
        print(unumber)
        price = request.POST.get("price")
        print(price)

        if form.is_valid():
            udate = request.POST.get("udate")
            ustartTime = request.POST.get("ustartTime")
            uendTime = request.POST.get("uendTime")
            title = request.POST.get("title")
            uprefix = request.POST.get("uprefix")
            ufirstname = request.POST.get("ufirstname")
            umiddlename = request.POST.get("umiddlename")
            ulastname = request.POST.get("ulastname")
            uage = request.POST.get("uage")
            ugender = request.POST.get("ugender")
            uaddress = request.POST.get("uaddress")
            uemail = request.POST.get("uemail")
            unumber = request.POST.get("unumber")
            price = request.POST.get("price")

        form = User(udate = udate, ustartTime=ustartTime, uendTime=uendTime, title_id=title,
                    uprefix = uprefix, ufirstname=ufirstname, umiddlename=umiddlename, ulastname=ulastname,
                    uage = uage, ugender = ugender, uaddress = uaddress, uemail = uemail, 
                    unumber = unumber, price_id = price)
        form.save()

        return redirect('reservation_user')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'corr/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'corr/upload.html', {'form': form})



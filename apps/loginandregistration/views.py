from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
# from django.contrib.auth.models import User
from . models import User
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NUMBER_IN_STRING_REGEX = re.compile(r'\d')
# from .models import Book, Author

# Create your views here.
def index(request):
    # messages.add_message(request, messages.INFO, 'Hello world.')
    # test_response_from_models = User.objects.test_function('test_string')
    return render(request,'loginandregistration/index.html')

def register(request):
    # Author.objects.create(name=request.POST['name'])
    response_from_models = User.objects.add_user(request.POST)
    # error = 0
    # if len(request.POST.get('first_name','')) <2:
    #     error += 1
    #     messages.add_message(request, messages.INFO, 'first name needs more characters')
    # # if NUMBER_IN_STRING_REGEX.match(request.POST.get('first_name','')):
    # #     error += 1
    # #     messages.add_message(request, messages.INFO, 'no numbers allowed in name')
    # if len(request.POST.get('last_name','')) <2:
    #     error += 1
    #     messages.add_message(request, messages.INFO, 'last name needs more characters')
    # # if NUMBER_IN_STRING_REGEX.match(request.POST.get('last_name','')):
    # #     error += 1
    # #     messages.add_message(request, messages.INFO, 'no numbers allowed in name')
    # if not EMAIL_REGEX.match(request.POST.get('email','')):
    #     error += 1
    #     messages.add_message(request, messages.INFO, 'email is not valid')
    # if len(request.POST.get('password','')) < 8:
    #     error +=1
    #     messages.add_message(request, messages.INFO, 'password needs to be 8 characters or more!')
    # if request.POST.get('password','') != request.POST.get('confirm',''):
    #     error +=1
    #     messages.add_message(request, messages.INFO, 'passwords do not match!')

    # if error ==0:
    #     hashed = bcrypt.hashpw((request.POST.get('password','')).encode(), bcrypt.gensalt())
    #     print hashed
    #         #  hashed2 = bcrypt.hashpw((request.POST.get('password','')).encode(), bcrypt.gensalt())
    #         #  print hashed2
    #     if bcrypt.checkpw(request.POST.get('password','').encode(), hashed):
    #             print "it matches"
    #     else:
    #             print "it does not match"
    #     # #     query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
    #     # #     data = { 'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'password': hashed }
    #     # #     mysql.query_db(query, data)
    #     #       messages.add_message(request, messages.INFO, 'Thanks for registering!')
    #     return redirect('/')
    return redirect('/')

def login(request):
    # author = Author.objects.get(id=request.POST['author'])
    # Book.objects.create(title= request.POST['title'], author = author)
    # Check that a unhashed password matches one that has previously been
        #   hashed
        # saved_hashed = bcrypt.hashpw(12345678).encode(), bcrypt.gensalt())
        # if bcrypt.hashpw(password, hashed) == hashed:
        #     print("It Matches!")
        # else:
        #     print("It Does not Match :(")
    # user = self.filter(email = postData['email'])
    # if user:
    #    error.append('Email already exists')

    # modelResponse{}
    # FAILED VAlIDATIONS - send to Views page
    # if errors:
    #   modelResponse['status'] = False
    #   modelResponse['errors'] = errors
    #
    # else:
    

    return redirect('/')

# def addBook(request):
#     if request.method == 'POST':
#         # print request.POST
#         Book.objects.add_book(request.POST)
#     return redirect('books:index')
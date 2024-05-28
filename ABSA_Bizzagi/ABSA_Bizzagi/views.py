from django.shortcuts import render
import pyrebase


config={
	"apiKey": "AIzaSyAEjIqr3gvGZmST9CrkRVwAxdYOf-6g7Kk",
	"authDomain": "bizzagi-ea16d.firebaseapp.com",
	"databaseURL": "https://bizzagi-ea16d-default-rtdb.asia-southeast1.firebasedatabase.app",
	"projectId": "bizzagi-ea16d",
	"storageBucket": "bizzagi-ea16d.appspot.com",
	"messagingSenderId": "105672477056",
	"appId": "1:105672477056:web:7b4fcd245c900d7bbcd965"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def signIn(request):
	return render(request,"Login.html")
def home(request):
	return render(request,"Home.html")

def postsignIn(request):
	email=request.POST.get('email')
	pasw=request.POST.get('pass')
	try:
		user=authe.sign_in_with_email_and_password(email,pasw)
	except:
		message="Invalid Credentials!!Please ChecK your Data"
		return render(request,"Login.html",{"message":message})
	session_id=user['idToken']
	request.session['uid']=str(session_id)
	return render(request,"Home.html",{"email":email})

def logout(request):
	try:
		del request.session['uid']
	except:
		pass
	return render(request,"Login.html")

def signUp(request):
	return render(request,"Registration.html")

def postsignUp(request):
	email = request.POST.get('email')
	passs = request.POST.get('pass')
	name = request.POST.get('name')
	try:
		# creating a user with the given email and password
		user=authe.create_user_with_email_and_password(email,passs)
		uid = user['localId']
		idtoken = request.session['uid']
		print(uid)
	except:
		return render(request, "Registration.html")
	return render(request,"Login.html")

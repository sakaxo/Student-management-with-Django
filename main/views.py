from django.shortcuts import render,get_object_or_404,redirect
from main.models import Student
from django.contrib import messages


def home(request):
	title = 'Student records '
	students = Student.objects.all().order_by('-id').values()

	context = {
	'page_title': title,
	'students':students


	}

	return render(request,'main/index.html',context)




def admit(request):
	title = 'Add New Student '
	context = {'page_title': title}

	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')

		s = Student(fname=fname,lname=lname,email=email)
		s.save()
		# messages.success(request, 'Student added successfully.')

		return redirect('home')

	return render(request,'main/add_student.html', context)




def delete_student(request,pk):
	student_id = pk
	student = get_object_or_404(Student, pk=student_id)
	student.delete()

	return redirect('home')



def edit(request, pk):
	u = get_object_or_404(Student, pk=pk)

	if request.method == "POST":
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')

		u.fname = fname
		u.lname	=lname
		u.email = email
		u.save()

		return redirect('home')

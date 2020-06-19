from django.shortcuts import render
from testApp.models import Student,Teacher,ProxyTeacher
# Create your views here.
def student_view(request):
    student_list=Student.objects.all()
    return render(request,'testApp/student.html',{'student_list':student_list})
def teacher_view(request):
    teacher_list=Teacher.objects.all()
    return render(request,'testApp/teacher.html',{'teacher_list':teacher_list})
def ascending_view(request):
    teacher_list=ProxyTeacher.objects1.all()
    return render(request,'testApp/teacher.html',{'teacher_list':teacher_list})
def descending_view(request):
    teacher_list=ProxyTeacher.objects2.all()
    return render(request,'testApp/teacher.html',{'teacher_list':teacher_list})
def above15k_view(request):
    teacher_list=ProxyTeacher.objects3.all()
    return render(request,'testApp/teacher.html',{'teacher_list':teacher_list})

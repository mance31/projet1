from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student,Presence
from .form import StudentForm,callform,cursuscallform
#from .formcall import callform
from django.views.generic import CreateView,UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE

#page d'accueil
def index (request):
  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

#afficher les étudiants correspondant à un cursus
def detail(request, cursus_id):
  #nom=Student.objects.all()
  #result_list=Student.objects.get(user = request.first_name)
  #resp = "result for cursus {}".format(nom)
  
  result_list = Student.objects.filter(cursus=cursus_id)
  
  #curs=Cursus.object.get('name')
  #result_list = get_object_or_404(Student, pk=student_id)
  #result = Cursus.objects.order_by('name')
  # context
  
  context = {'liste': result_list,
                        
            }
  return render (request, 'lycee/detail.html' , context)
  #return HttpResponse(resp,nom)

def detail_student(request,student_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = get_object_or_404(Student, pk=student_id)
    # context
    context = {'liste': result_list,}
    return render (request, 'lycee/student/detail_student.html' , context)
    
#création d'un étudiant    
class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"

  # page appelEe si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

#modification d'un étudiant
class editstudent(UpdateView):
  #editstud = Student.objects.get(student_id)
  #student=Student.objects.get(student=student_id)
  #model=StudentForm
  #if request.method=="POST":
  #  form=editstudent(request.POST, request.student)
  #  if form.is_valid():
  #    form.save()
  #    return redirect('/lycee/student/{{student_id}}')
  #else:
  #  form=editstudent(request.student)

    #result_list = get_object_or_404(Student, pk=student_id)
  #  context = {'liste': form,}
  #  return render (request, 'lycee/student/edit/editstudent.html' , context)
  #return render (request,"lycee/student/editsudent.html",{"Student :":editstud})
  model=Student
  form_class=StudentForm
  template_name="lycee/edit/editstudent_edit.html"
  template_name_suffix="_edit"

  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

#page apppel effectué pour le particular call of roll
def calleffec(request,presence_id):
  result_list = get_object_or_404(Presence, pk=presence_id)
    # context
  #context = {'liste': result_list,}
  #result_list = Presence.objects.order_by('Reasson')
  # contexte
  context = { 'liste' : result_list}
  
  return render (request, 'lycee/call/calleffec.html', context)

# particular call of roll
class call(CreateView):
  model = Presence
  form_class = callform
  template_name = "lycee/call/call.html"

  def get_success_url(self):
    return reverse("calleffec", args=(self.object.pk,))

#def curscalleffect(request,presence_id):
  #result_list = Student.objects.get(pk=student_id)
 # result_list = get_object_or_404(Presence, pk=presence_id)

# context = {'liste': result_list,}
#  return render (request, 'lycee/cursuscall/curscalleffect.html', context)

#class cursuscall(CreateView):
#  model = Presence
#  form_class = cursuscallform
#  template_name="lycee/cursuscall/callcursus.html"

#  def get_success_url(self):
#    return reverse("curscalleffect", args=(self.object.pk,))

#call of roll
def callcursus(request,cursus_id):
  result_list = Student.objects.filter(cursus=cursus_id)
  students = Student.objects.order_by("student.id")
  if request.method == 'POST': 
    date = request.POST.get("date_call") 
    for students in students:
      ismissing = request.POST.get('student '+str(students.id), "off")
#    def get_success_url(self):
#      return reverse("curscalleffect", args=(self.object.pk,)) 
  
  context = {'liste': result_list,                      
            }
  return render (request, 'lycee/cursuscall/callcursus.html', context)
  
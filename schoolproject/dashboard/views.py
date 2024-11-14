from django.shortcuts import render
from .models import CompFirstYear, CompFourthYear, CompSecondYear, CompThirdYear, BeedFirstYear, BeedSecondYear, BeedThirdYear # Ensure this import is at the top
from .models import BeedFourthYear, BtledFirstYear, BtledSecondYear, BtledThirdYear, BtledFourthYear, CivilFirstYear, CivilSecondYear
from .models import CivilThirdYear, CivilFourthYear, ElectFirstYear, ElectSecondYear,ElectThirdYear, ElectFourthYear, MechaFirstYear, MechaSecondYear
from .models import MechaThirdYear, MechaFourthYear, AutoFirstYear, AutoSecondYear, AutoThirdYear, AutoFourthYear, ComgentFirstYear, ComgentSecondYear
from .models import ComgentThirdYear, ComgentFourthYear

# Home page view
def index(request):
    courses = None

    if request.method == 'POST':
        year = request.POST.get('year')
        course_type = request.POST.get('course_type')


                # Query for SecondYear courses
        if year == '2' and course_type == 'comptech':
            courses = CompSecondYear.objects.all()  # Adjust your query based on your actual filtering logic

        elif year == '2' and course_type == 'beed':
            courses = BeedSecondYear.objects.all()  

        elif year == '2' and course_type == 'btled':
            courses = BtledSecondYear.objects.all() 

        elif year == '2' and course_type == 'civil':
            courses = CivilSecondYear.objects.all()

        elif year == '2' and course_type == 'electrical':
            courses = ElectSecondYear.objects.all()

        elif year == '2' and course_type == 'mechanical':
            courses = MechaSecondYear.objects.all()

        elif year == '2' and course_type == 'automotive':
            courses = AutoSecondYear.objects.all()

        elif year == '2' and course_type == 'comgent':
            courses = ComgentSecondYear.objects.all()
            

                # Query for FirstYear courses
        elif year == '1' and course_type == 'comptech':
            courses = CompFirstYear.objects.all()  

        elif year == '1' and course_type == 'beed':
            courses = BeedFirstYear.objects.all() 

        elif year == '1' and course_type == 'btled':
            courses = BtledFirstYear.objects.all() 

        elif year == '1' and course_type == 'civil':
            courses = CivilFirstYear.objects.all() 

        elif year == '1' and course_type == 'electrical':
            courses = ElectFirstYear.objects.all()   

        elif year == '1' and course_type == 'mechanical':
            courses = MechaFirstYear.objects.all()  

        elif year == '1' and course_type == 'automotive':
            courses = AutoFirstYear.objects.all() 

        elif year == '1' and course_type == 'comgent':
            courses = ComgentFirstYear.objects.all() 


                # Query for ThirdYear courses
        elif year == '3' and course_type == 'comptech':
            courses = CompThirdYear.objects.all()  

        elif year == '3' and course_type == 'beed':
            courses = BeedThirdYear.objects.all()  

        elif year == '3' and course_type == 'btled':
            courses = BtledThirdYear.objects.all()

        elif year == '3' and course_type == 'civil':
            courses = CivilThirdYear.objects.all()

        elif year == '3' and course_type == 'electrical':
            courses = ElectThirdYear.objects.all()

        elif year == '3' and course_type == 'mechanical':
            courses = MechaThirdYear.objects.all()

        elif year == '3' and course_type == 'automotive':
            courses = AutoThirdYear.objects.all()

        elif year == '3' and course_type == 'comgent':
            courses = ComgentThirdYear.objects.all()



                # Query for FourthYear courses
        elif year == '4' and course_type == 'comptech':
            courses = CompFourthYear.objects.all()  

        elif year == '4' and course_type == 'beed':
            courses = BeedFourthYear.objects.all() 

        elif year == '4' and course_type == 'btled':
            courses = BtledFourthYear.objects.all()

        elif year == '4' and course_type == 'civil':
            courses = CivilFourthYear.objects.all() 

        elif year == '4' and course_type == 'electrical':
            courses = ElectFourthYear.objects.all() 

        elif year == '4' and course_type == 'mechanical':
            courses = MechaFourthYear.objects.all()

        elif year == '4' and course_type == 'automotive':
            courses = AutoFourthYear.objects.all()

        elif year == '4' and course_type == 'comgent':
            courses = ComgentFourthYear.objects.all()
            

    return render(request, 'index.html', {'courses': courses})

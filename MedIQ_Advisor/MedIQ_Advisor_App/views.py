from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from MedIQ_Advisor_App.models import Contact, Sign_up, Mental_Health_Survey, Heart_Health_Survey, Diabetes_Survey, Brain_Tumor_Survey
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def index_function(request):
    return render(request, 'MedIQ_Advisor_App_Template/index.html')
    # return render(request, 'index.html')

def sign_in_function(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")

        else:
            # No backend authenticated the credentials
            return render(request, 'MedIQ_Advisor_App_Template/sign_in.html')

    return render(request, 'MedIQ_Advisor_App_Template/sign_in.html')

def sign_up_function(request):
    if request.method == "POST":
        # Get data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        security_question = request.POST.get('security_question')
        security_question_answer = request.POST.get('security_question_answer')
        password = request.POST.get('password')
        
        # Check if the username already exists
        if Sign_up.objects.filter(username=username).exists():
            # If the username exists, show a message and redirect to the sign-up page
            messages.error(request, "Username already exists. Please choose a different username.")
            return redirect('/sign_up')  # Assuming 'signup' is the URL name for your sign-up page
        
        # If the username is unique, create a new User instance and save it to the database
        sign_up = Sign_up(first_name=first_name, last_name=last_name, email=email, username=username, security_question=security_question, security_question_answer=security_question_answer, password=password)
        sign_up.save()
        
        messages.success(request, "Sign up, successful!!")

    return render(request, 'MedIQ_Advisor_App_Template/sign_up.html')

from django.contrib.auth.models import User  # Assuming you're using Django's built-in User model

def forgot_password_function(request):
    if request.method == 'POST':
        # Get the username from the form
        username = request.POST['username']
        security_question_answer = request.POST['security_question_answer']

        # Check if the user exists
        try:
            user = User.objects.get(username=username)
            # Get user details like first_name, last_name, email, and security_question from the user object
            first_name = user.first_name
            last_name = user.last_name
            email = user.email
            security_question = user.security_question  # Replace 'security_question' with the actual field name in your model

            # Check if the user answered the security question correctly
            if request.POST['security_question_answer'] == user.security_question_answer:  # Replace 'security_answer' with the actual field name in your model
                # Provide the user's password in a secure way (e.g., email)
                password = user.password
                return render(request, 'MedIQ_Advisor_App_Template/forgot_password.html', {'password': password})
            else:
                messages.error(request, "Incorrect security question's answer!!")
                # return render(request, 'MedIQ_Advisor_App_Template/forgot_password.html', {'error_message': 'Incorrect security answer'})
        except User.DoesNotExist:
             messages.error(request, "User not found!!")

    return render(request, 'MedIQ_Advisor_App_Template/forgot_password.html')


def home_function(request):
    return render(request, 'MedIQ_Advisor_App_Template/home.html')

def contact_function(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!!")
        
    return render(request, 'MedIQ_Advisor_App_Template/contact.html')

def emotion_questionnaire_function(request):
    if request.method == 'POST':
        # Retrieve data from the form
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        self_employed = request.POST.get('selfEmployed')
        family_history = request.POST.get('familyHistory')
        mental_health_interference = request.POST.get('mentalHealthInterference')
        company_size = request.POST.get('companySize')
        remote_work = request.POST.get('remoteWork')
        tech_company = request.POST.get('techCompany')
        mental_health_benefits = request.POST.get('mentalHealthBenefits')
        know_mental_health_care = request.POST.get('knowMentalHealthCare')
        discussed_mental_health = request.POST.get('discussedMentalHealth')
        resources_learn_mental_health = request.POST.get('resourcesLearnMentalHealth')
        anonymity_protected = request.POST.get('anonymityProtected')
        medical_leave = request.POST.get('medicalLeave')
        negative_consequences_mental_health = request.POST.get('negativeConsequencesMentalHealth')
        negative_consequences_physical_health = request.POST.get('negativeConsequencesPhysicalHealth')
        discuss_with_coworkers = request.POST.get('discussWithCoworkers')
        discuss_with_supervisors = request.POST.get('discussWithSupervisors')
        bring_up_in_interview_mental_health = request.POST.get('bringUpInInterviewMentalHealth')
        bring_up_in_interview_physical_health = request.POST.get('bringUpInInterviewPhysicalHealth')
        employer_takes_mental_health_seriously = request.POST.get('employerTakesMentalHealthSeriously')
        observed_negative_consequences = request.POST.get('observedNegativeConsequences')

        # Save the survey data to the database
        survey_data = Mental_Health_Survey(
            age=age,
            gender=gender,
            self_employed=self_employed,
            family_history=family_history,
            mental_health_interference=mental_health_interference,
            company_size=company_size,
            remote_work=remote_work,
            tech_company=tech_company,
            mental_health_benefits=mental_health_benefits,
            know_mental_health_care=know_mental_health_care,
            discussed_mental_health=discussed_mental_health,
            resources_learn_mental_health=resources_learn_mental_health,
            anonymity_protected=anonymity_protected,
            medical_leave=medical_leave,
            negative_consequences_mental_health=negative_consequences_mental_health,
            negative_consequences_physical_health=negative_consequences_physical_health,
            discuss_with_coworkers=discuss_with_coworkers,
            discuss_with_supervisors=discuss_with_supervisors,
            bring_up_in_interview_mental_health=bring_up_in_interview_mental_health,
            bring_up_in_interview_physical_health=bring_up_in_interview_physical_health,
            employer_takes_mental_health_seriously=employer_takes_mental_health_seriously,
            observed_negative_consequences=observed_negative_consequences
        )
        survey_data.save()
        messages.success(request, "Your data has been recorded!!")

    return render(request, 'MedIQ_Advisor_App_Template/emotion_questionnaire.html')

def heart_health_function(request):
    if request.method == 'POST':
        # Retrieve data from the form
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        chest_pain = request.POST.get('chestPain')
        resting_blood_pressure = request.POST.get('restingBP')
        serum_cholesterol = request.POST.get('cholesterolLevel')
        high_fasting_blood_sugar = request.POST.get('highFastingBloodSugar')
        resting_ecg = request.POST.get('restingECG')
        max_heart_rate = request.POST.get('maxHeartRate')
        exercise_induced_angina = request.POST.get('exerciseInducedAngina')
        st_depression = request.POST.get('stDepression')
        peak_exercise_st_slope = request.POST.get('peakExerciseSTSlope')
        colored_vessels = request.POST.get('coloredVessels')
        thalassemia_type = request.POST.get('thalassemiaType')

        # Save the survey data to the database
        survey_data = Heart_Health_Survey(
            age=age,
            gender=gender,
            chest_pain=chest_pain,
            resting_blood_pressure=resting_blood_pressure,
            serum_cholesterol=serum_cholesterol,
            high_fasting_blood_sugar=high_fasting_blood_sugar,
            resting_ecg=resting_ecg,
            max_heart_rate=max_heart_rate,
            exercise_induced_angina=exercise_induced_angina,
            st_depression=st_depression,
            peak_exercise_st_slope=peak_exercise_st_slope,
            colored_vessels=colored_vessels,
            thalassemia_type=thalassemia_type
        )
        survey_data.save()
        messages.success(request, "Your data has been recorded!!")

    return render(request, 'MedIQ_Advisor_App_Template/heart_health.html')

def diabetes_function(request):
    if request.method == 'POST':
        # Retrieve data from the form
        pregnancies = request.POST.get('pregnancies')
        glucose_level = request.POST.get('glucoseLevel')
        blood_pressure = request.POST.get('bloodPressure')
        skin_thickness = request.POST.get('skinThickness')
        insulin_level = request.POST.get('insulinLevel')
        bmi = request.POST.get('bmi')
        diabetes_pedigree = request.POST.get('diabetesPedigree')
        age = request.POST.get('age')

        # Save the survey data to the database
        survey_data = Diabetes_Survey(
            pregnancies=pregnancies,
            glucose_level=glucose_level,
            blood_pressure=blood_pressure,
            skin_thickness=skin_thickness,
            insulin_level=insulin_level,
            bmi=bmi,
            diabetes_pedigree=diabetes_pedigree,
            age=age
        )
        survey_data.save()
        messages.success(request, "Your data has been recorded!!")

    return render(request, 'MedIQ_Advisor_App_Template/diabetes.html')

def brain_tumor_function(request):
    if request.method == 'POST':
        # Retrieve data from the form
        brain_tumor_diagnosis = request.POST.get('brainTumorDiagnosis')
        mean_radius = request.POST.get('meanRadius')
        mean_texture = request.POST.get('meanTexture')
        mean_perimeter = request.POST.get('meanPerimeter')
        mean_area = request.POST.get('meanArea')
        smoothness = request.POST.get('smoothness')
        mean_compactness = request.POST.get('meanCompactness')
        concavity = request.POST.get('concavity')
        concave_points = request.POST.get('concavePoints')
        symmetry = request.POST.get('symmetry')
        mean_fractal_dimension = request.POST.get('meanFractalDimension')
        se_radius = request.POST.get('seRadius')
        se_texture = request.POST.get('seTexture')
        se_perimeter = request.POST.get('sePerimeter')
        se_area = request.POST.get('seArea')
        se_smoothness = request.POST.get('seSmoothness')
        se_compactness = request.POST.get('seCompactness')
        se_concavity = request.POST.get('seConcavity')
        se_concave_points = request.POST.get('seConcavePoints')
        se_symmetry = request.POST.get('seSymmetry')
        se_fractal_dimension = request.POST.get('seFractalDimension')
        worst_radius = request.POST.get('worstRadius')
        worst_texture = request.POST.get('worstTexture')
        worst_perimeter = request.POST.get('worstPerimeter')
        worst_area = request.POST.get('worstArea')
        worst_smoothness = request.POST.get('worstSmoothness')
        worst_compactness = request.POST.get('worstCompactness')
        worst_concavity = request.POST.get('worstConcavity')
        worst_concave_points = request.POST.get('worstConcavePoints')
        worst_symmetry = request.POST.get('worstSymmetry')
        worst_fractal_dimension = request.POST.get('worstFractalDimension')

        # Save the survey data to the database
        survey_data = Brain_Tumor_Survey(
            brain_tumor_diagnosis=brain_tumor_diagnosis,
            mean_radius=mean_radius,
            mean_texture=mean_texture,
            mean_perimeter=mean_perimeter,
            mean_area=mean_area,
            smoothness=smoothness,
            mean_compactness=mean_compactness,
            concavity=concavity,
            concave_points=concave_points,
            symmetry=symmetry,
            mean_fractal_dimension=mean_fractal_dimension,
            se_radius=se_radius,
            se_texture=se_texture,
            se_perimeter=se_perimeter,
            se_area=se_area,
            se_smoothness=se_smoothness,
            se_compactness=se_compactness,
            se_concavity=se_concavity,
            se_concave_points=se_concave_points,
            se_symmetry=se_symmetry,
            se_fractal_dimension=se_fractal_dimension,
            worst_radius=worst_radius,
            worst_texture=worst_texture,
            worst_perimeter=worst_perimeter,
            worst_area=worst_area,
            worst_smoothness=worst_smoothness,
            worst_compactness=worst_compactness,
            worst_concavity=worst_concavity,
            worst_concave_points=worst_concave_points,
            worst_symmetry=worst_symmetry,
            worst_fractal_dimension=worst_fractal_dimension
        )
        survey_data.save()
        messages.success(request, "Your data has been recorded!!")

    return render(request, 'MedIQ_Advisor_App_Template/brain_tumor.html')
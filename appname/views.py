import pickle
from django.shortcuts import render


# Create your views here.
def home(request):
    with open('C:\\Users\\USER\\Desktop\\pickle proj\\appname\\model.pkl', 'rb') as f:
        model = pickle.load(f)
        print(model)
    if request.method == 'POST':
        Gender = request.POST['Gender']
        Married = request.POST['Married']
        Education = request.POST['Education']
        Self_Employed = request.POST['Self_Employed']
        ApplicantIncome = request.POST['ApplicantIncome']
        CoapplicantIncome = request.POST['CoapplicantIncome']
        LoanAmount = request.POST['LoanAmount']
        Loan_Amount_Term = request.POST['Loan_Amount_Term']
        Credit_History = request.POST['Credit_History']
        Property_Area = request.POST['Property_Area']
        pred = model.predict([[Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,
                              LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]])
        print(pred[0])
        # ['Gender'].map({'Male': 1, 'Female': 0})
        # ['Married'].map({'Yes': 1, 'No': 0})
        # ['Education'].map({'Graduate': 1, 'Not Graduate': 0})
        # ['Self_Employed'].map({'Yes': 1, 'No': 0})
        # ['Property_Area'].map({'Urban': 0, 'Semiurban': 1, 'Rural': 2})
        if pred[0] == 1:
            result = "Eligible"
        else:
            result = "Not Elgible"
        return render(request, 'appname/home.html',{'prediction':result})

    return render(request, 'appname/home.html')

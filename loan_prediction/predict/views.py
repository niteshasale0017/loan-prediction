from django.shortcuts import render,HttpResponse
import joblib
import numpy as np
# Create your views here.
model = joblib.load('loan_prediction.pkl')


def home(request):
	return render(request,'predict/home.html')

def predict(request):
	if request.method=="POST":
		gender = request.POST.get('gender')
		marital_status = request.POST.get('marital_status')
		dependents = request.POST.get('dependents')
		education = request.POST.get('education')
		self_employed = request.POST.get('self_employed')
		applicant_income = request.POST.get('applicant_income')
		coapplicant_income = request.POST.get('coapplicant_income')
		loan_amount = request.POST.get('loan_amount')
		loan_amount_term = request.POST.get('loan_amount_term')
		credit_history = request.POST.get('credit_history')
		property_area = request.POST.get('property_area')
		all_data = [gender,marital_status,dependents,education,self_employed,applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,property_area]
		new_add_data = []
		for i in all_data:
			if i  == '0' or i=='no' or i=='female' or i=='not graduate' or i=='unmarried' or i=='rural' or i=='0.0':
				new_add_data.append(0)
			elif i == '1' or i=='male' or i=='married' or i=='graduate' or i=='yes' or i=='semiurban' or i=='1.0':
				new_add_data.append(1)
			elif i == '2' or i=='urban':
				new_add_data.append(2)
			elif i == '3':
				new_add_data.append(3)	
			else:
				new_add_data.append(i)	
		
		print('*************')
		print(new_add_data)
		output = np.array([new_add_data])
		final = model.predict(output)				
		data = str(final[0])
		print(data)
		print(type(data))
	return render(request,'predict/home.html',{'data':data})

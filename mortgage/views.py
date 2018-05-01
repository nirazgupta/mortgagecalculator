from django.shortcuts import render,redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.urlresolvers import reverse, resolve
from mortgage.models import User, Loan
import decimal
from decimal import Decimal, ROUND_UP
# Create your views here.
def index(request):
    return render(request, 'mortgage/index.html')

def loan(request):
    if request.method == 'POST':
        return redirect('show_data')
        #return render_to_response('mortgage/show_data.html', context)
    return render(request, 'mortgage/loan.html')

def user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        #mortgage_name = request.POST.get('mortgage_name')

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            user_obj = User(name = name, email = email)
            user_obj.save()
        request.session['email'] = email
        request.session['name'] = name

        #print(request.session.get('email'))
        context = {'name': name, 'email': email}
        return render(request, 'mortgage/user.html', context)
    return render(request, 'mortgage/user.html')

def show_data(request):
    if request.method == 'POST':
        loan_name = request.POST.get('loan_name')
        amount = request.POST.get('loan_amount')
        raw_year = request.POST.get("year")
        month = request.POST.get("month")
        rate = request.POST.get("rate")
        downpayment = request.POST.get("down_payment")
        add_monthly_payment = request.POST.get("add_per_month")
        add_yearly_payment = request.POST.get("add_per_year")

        principle = decimal.Decimal(amount)  - decimal.Decimal(downpayment)

        sess_email = request.session.get('email')
        user_data = User.objects.all().filter(email=sess_email)
        
        user_id_ls = []
        for item in user_data:
            user_id_ls.append(item.id)

        user_id = user_id_ls[0]

        loan_obj = Loan(user_id=user_id, loan_amount= amount, year = raw_year,
                        month = month, rate = rate, loan_name=loan_name,
                        down_payment=downpayment, add_per_month=add_monthly_payment, add_per_year=add_yearly_payment)
        loan_obj.save()


        return redirect('/mortgage/show_configs/')
    return render(request, 'mortgage/show_data.html')

def show_configs(request):
    sess_email = request.session.get('email')
    user_data = User.objects.all().filter(email=sess_email)
    
    user_id_ls = []
    for item in user_data:
        user_id_ls.append(item.id)
        #print(item.id)

    user_id = user_id_ls[0]
    loan_data = Loan.objects.all().filter(user_id=user_id)
    return render(request, 'mortgage/show_configs.html', {'loan_data': loan_data})

# def loan_config_detail(request, id=id):
#     if request.method == POST:
#         loan_config_data = Loan.objects.all().filter(id=id)
#     return render(request, 'mortgage/loan_config_detail.html', {'loan_config_data': loan_config_data})
    #return render(request, 'mortgage/loan.html')

def loan_config_detail(request, id):
    loan_data = get_object_or_404(Loan, pk=id)

    amount_frm_db = loan_data.loan_amount
    downpayment = loan_data.down_payment
    year_frm_db = loan_data.year
    month_frm_db = loan_data.month
    rate_frm_db = loan_data.rate
    add_monthly_payment_db = loan_data.add_per_month
    add_yearly_payment_db  = loan_data.add_per_year
    print(add_monthly_payment_db)
    print(add_yearly_payment_db)

    if add_monthly_payment_db > 0 and add_yearly_payment_db == 0:
        extra_payment_amt = add_monthly_payment_db
    elif add_monthly_payment_db == 0 and add_yearly_payment_db > 0:
        split_yearly = add_yearly_payment_db/12
        extra_payment_amt = split_yearly
    else:
        extra_payment_amt = 0

    print(extra_payment_amt)
    #Loan amount minus the downpayment
    borrowed_amt = amount_frm_db - downpayment
   # print(borrowed_amt)
    #print(amount_frm_db, year_frm_db, month_frm_db, rate_frm_db)

    #calculate term by multiplying year_frm_db with 12 then adding it with the month (entered by user)
    term = (int(year_frm_db)*12) + int(month_frm_db)
    #print(term)
    #calculate monthly interest by dividing rate by 100 to get decimal from percentage and again by 12 to make it monthly i.e rate/(100*12)
    interest = rate_frm_db/1200

    # interest * amount_frm_db give the total interest for month
    # note var beginning with _ means partial variable
    _tot_interest = interest * borrowed_amt
    #_tot_interest rounded to 2 decimal points
    tot_interest = round(_tot_interest, 2)

    # monthly payment calculation using (P * (i * (1 + i) ** n )/ ((1 + i) ** n -1) 
    _monthly_payment = borrowed_amt * (interest * (1 + interest) ** term) / ((1 + interest) ** term - 1) 

    ##Generating the ammortization table
    beginning_bal = Decimal(borrowed_amt)
    ammortization_data = []
    rounded_ammortization_data = []

    for i in range(1, term+1):       
        monthly_payment = round(_monthly_payment,5)
        tbl_interest = round(beginning_bal * (rate_frm_db / (12 * 100)),5)
        #print(tbl_interest)
        principle = monthly_payment - tbl_interest
        
        if principle < beginning_bal and add_monthly_payment_db == 0 and add_yearly_payment_db == 0:
            ending_bal = beginning_bal - principle       
            beginning_bal = ending_bal
        elif principle + extra_payment_amt < beginning_bal and add_monthly_payment_db > 0 and add_yearly_payment_db == 0:            
            ending_bal = beginning_bal - (principle + extra_payment_amt)      
            beginning_bal = ending_bal
        elif principle + extra_payment_amt < beginning_bal and add_monthly_payment_db == 0 and add_yearly_payment_db > 0:
            ending_bal = beginning_bal - (principle + extra_payment_amt)  
            beginning_bal = ending_bal
        else:
            break

        dict = {"term": i, 'montly_pmt': monthly_payment, 'beginning_bal': beginning_bal, 
                "interest": tbl_interest, "extra_pmt": extra_payment_amt, 
                "principle": principle, 'ending_bal':ending_bal}
        ammortization_data.append(dict)

        
        dict_2 = {"term": i, 'montly_pmt': round(monthly_payment,2), "interest": round(tbl_interest,2), 
                "extra_pmt": round(extra_payment_amt,2), 
                "principle": round(principle,2), 'ending_bal': round(ending_bal,2)}

        rounded_ammortization_data.append(dict_2)


    last_itm_frm_dict = ammortization_data[-1]
    rem_end_bal = last_itm_frm_dict['ending_bal']
    #print(rem_end_bal)

    rem_interest = (rate_frm_db/(12*100)) * rem_end_bal
    #print(rem_interest)

    monthly_payment_rounded = round(monthly_payment,2)
    total_interest = round(sum(item['interest'] for item in ammortization_data) + rem_interest, 2)
    regular_principle = round(sum(item['principle'] for item in ammortization_data) + rem_end_bal ,2) 
    extra_principle = round(sum(item['extra_pmt'] for item in ammortization_data),2)
    payoff_period = len(ammortization_data)
    total_principle = round(regular_principle + extra_principle, 2) 
    total_payments = round(total_interest + regular_principle + extra_principle, 2)
    total_savings = round((term * monthly_payment - borrowed_amt) - (total_payments - total_principle), 2)


    context = {'term':term,'monthly_payment': monthly_payment_rounded, 'interest': interest, 
                'tot_interest': total_interest, 'reg_principle': regular_principle,
                 'rate':rate_frm_db, 'extra_principle': extra_principle, 'total_principle': total_principle,
                'total_payments': total_payments, 'total_savings': total_savings, 'payoff_period': payoff_period}


    return render(request, 'mortgage/loan_config_detail.html', {'brwd_amt':borrowed_amt, 'loan_data': loan_data,
                 'context':context, 'ammortization_data' : rounded_ammortization_data})


def delete(request, id):
   loan_record = get_object_or_404(Loan, pk=id)
   loan_record.delete()
   return redirect('/mortgage/show_configs/')

def clear_session(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request, 'mortgage/user.html')

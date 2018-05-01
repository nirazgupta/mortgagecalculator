# mortgagecalculator
Web application developed using Django framework to calculate mortgage using the inputs from user.

# Features
* Login:
The application takes users name and email address to create a login session if the user has already registered. If user has not registered, the app takes those parameters to create an account. A password authentication is not implemented in this app due to scope and design of this application.
![alt text](https://github.com/nirazgupta/mortgagecalculator/blob/master/project_images/Login.PNG)

* Loan form:
Once the user logs in, the app brings a form for user to enter the configuration of the loan the he/she wants to calculate. Which includes a name of the configuration, loan amount, duration of loan, interest rate. The user is given extra payment options such using which they can add extra monthly payment amount or extra yearly payment amount and they can also add downpayments to the loan if they wish.  
![alt text](https://github.com/nirazgupta/mortgagecalculator/blob/master/project_images/loan_form.PNG)

* List view of configs:
User can view the list of their configurations using which they can compare different mortgages. For each mortgage configurations, user can view the borrowed amount, duration, payoff period, interest accrued, monthly payments, principle, total savings. User can also view the ammortization table for the particular mortgage configuration.
![alt text](https://github.com/nirazgupta/mortgagecalculator/blob/master/project_images/loanConfList.PNG)

* Mortgage calculation with payment options:
While creating a mortgage calculation configuration, user has option to leave the extra payments option blank due which monthly or yearly extra payments will not be taken into consideration, same applies for downpayments. 


![alt text](https://github.com/nirazgupta/mortgagecalculator/blob/master/project_images/withoutEP.PNG)
![alt text](https://github.com/nirazgupta/mortgagecalculator/blob/master/project_images/withoutEP2.PNG)

Else user can use the combinations of extra montly payments or yearly payments with downpayment to generate the calculation with ammortization schedule. They can also only select the downpayment if they like.

![alt text](https://github.com/nirazgupta/mortgagecalculator/blob/master/project_images/withMonthlyEp.PNG)


![alt text](https://github.com/nirazgupta/mortgagecalculator/blob/master/project_images/withAnnualEP.PNG)


![alt text](https://github.com/nirazgupta/mortgagecalculator/blob/master/project_images/withDownPayment.PNG)

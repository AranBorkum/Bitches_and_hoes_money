from pylab import *

#####################################
#Input variables - You can change these

starting_capital=50000.
yearly_contribution=0.
average_house_valuation=100000.
average_house_price=80000.
mortgage_term=15
interest_rate=0.06
landlords_insurance=20
rental_insurance=5
maintenance_fund_contribution=100
management_fees=100
investment_period=30
lifespan=70
minimum_maintenance_fund=0.5*average_house_valuation

#####################################
#Calculated variables

outright_owned_property=0
downpayment=0.25*average_house_valuation
mortgage_value=0.75*average_house_valuation
mortgage_repayment=mortgage_value*(interest_rate/12)/(1-(1+interest_rate/12)**(-12*mortgage_term))
rent=0.01*average_house_valuation
payment_schedule=zeros((2,int(mortgage_term*12+1)),dtype='float')
payment_level=[]
income=rent-mortgage_repayment-management_fees-rental_insurance-landlords_insurance

#####################################
#Repayment schedule calculator
#This is encoded in the mortgage_calculator function in future versions

principal=mortgage_value
for i in range(0,int(mortgage_term*12+1)):
    
    interest_contribution=interest_rate*principal/12
    principal_contribution=mortgage_repayment-interest_contribution
    
    payment_schedule[0,i]=interest_contribution
    payment_schedule[1,i]=principal_contribution
    
    principal-=principal_contribution

    if (i+1)%12==0 and 12*15>i>3:#this section calculates the year-end outstanding principle
        payment_level.append(principal)

#####################################
#Fund and record definitions

reinvestment_fund=starting_capital
maintenance_fund=0.
debt=zeros((1,lifespan),dtype='int')
equity=zeros((1,lifespan),dtype='int')
reinvestment=zeros((1,lifespan),dtype='int')
owned_property=zeros((1,lifespan),dtype='int')

#####################################
#Analysis

property_status=zeros((mortgage_term,lifespan),dtype='int') #a record of how many properties in each payment level we have at the end of the year
current_year_status=zeros((mortgage_term),dtype='int')#a place holder for where we start the year, property payment level wise

#Investment (i.e. no touchy) phase
for i in range(0,investment_period):
    
    #Beginning of year
    if reinvestment_fund>downpayment:
        current_year_status[0]=(reinvestment_fund-reinvestment_fund%downpayment)/downpayment
        reinvestment_fund-=(reinvestment_fund-reinvestment_fund%downpayment)

    #End of year
    debt_tally=0.
    property_tally=0
    for k in range(mortgage_term):
        debt_tally+=(current_year_status[k]*payment_level[k])
        property_tally+=current_year_status[k]
    debt[0,i]=debt_tally
    equity[0,i]=average_house_valuation*property_tally-debt_tally

    #Here, I fill funds and allocate income
    if maintenance_fund<minimum_maintenance_fund:
        maintenance_fund+=property_tally*maintenance_fund_contribution*12
        reinvestment_fund+=property_tally*(income-maintenance_fund_contribution)*12+outright_owned_property*(income+mortgage_repayment-maintenance_fund_contribution)*12
    elif maintenance_fund>=minimum_maintenance_fund:
        reinvestment_fund+=property_tally*(income)*12+outright_owned_property*(income+mortgage_repayment)

    reinvestment[0,i]=reinvestment_fund

    #Here, I copy the current year's record to the property status database.
    for j in range(mortgage_term):
        property_status[j,i]=current_year_status[j]

    owned_property[0,i]=outright_owned_property

    #In this section, we cycle properties for the next year, and knock some off the chain if they get payed off
    outright_owned_property+=current_year_status[mortgage_term-1]
    for j in range(mortgage_term+1):
        if mortgage_term-j > 0:
            current_year_status[mortgage_term-j-1]=current_year_status[mortgage_term-j-2]
        elif mortgage_term-j-1 ==0:
            current_year_status[mortgage_term-j-1]=0

#Debt Forgiveness phase ---- NEEDS A LOT OF WORK!!!
for i in range(investment_period,lifespan):
    
    #Beginning of year
    #In this section, we see how many properties we can pay off.
    for a in range(mortgage_term-1):
        if current_year_status[mortgage_term-1-a]==0:
            continue
        elif current_year_status[mortgage_term-a-1]!=0:
            while reinvestment_fund>payment_level[mortgage_term-1-a] and current_year_status[mortgage_term-a-1]!=0:
                reinvestment_fund-=payment_level[mortgage_term-1-a]
                outright_owned_property+=1
                current_year_status[mortgage_term-a-1]-=1

    if max(current_year_status)==0:
        while reinvestment_fund>average_house_price:
            reinvestment_fund-=average_house_price
            outright_owned_property+=1

    #End of year
    debt_tally=0.
    property_tally=0
    for k in range(mortgage_term):
        debt_tally+=(current_year_status[k]*payment_level[k])
        property_tally+=current_year_status[k]
    debt[0,i]=debt_tally
    equity[0,i]=average_house_valuation*(property_tally+outright_owned_property)-debt_tally

    #In this section, we adjust income based on the fact that we no longer pay mortgage repayments
    if maintenance_fund<minimum_maintenance_fund:
        maintenance_fund+=property_tally*maintenance_fund_contribution*12+outright_owned_property*maintenance_fund_contribution*12
        reinvestment_fund+=property_tally*(income-maintenance_fund_contribution)*12+outright_owned_property*(income+mortgage_repayment-maintenance_fund_contribution)*12
    elif maintenance_fund>=minimum_maintenance_fund:
        reinvestment_fund+=property_tally*(income)*12+outright_owned_property*(income+mortgage_repayment)*12

    reinvestment[0,i]=reinvestment_fund

    #Here, I copy the current year's record to the property status database.
    for j in range(mortgage_term):
        property_status[j,i]=current_year_status[j]

    owned_property[0,i]=outright_owned_property

    #In this section, we cycle properties to the next payment level for the next year
    for j in range(mortgage_term+1):
        if mortgage_term-j > 0:
            current_year_status[mortgage_term-j-1]=current_year_status[mortgage_term-j-2]
        elif mortgage_term-j-1 ==0:
            current_year_status[mortgage_term-j-1]=0

total_record=zeros((mortgage_term+4,lifespan),dtype='float')

for i in range(mortgage_term):
    for j in range(lifespan):
        total_record[i,j]=property_status[i,j]

for i in range(lifespan):
    total_record[mortgage_term,i]=debt[0,i]

for i in range(lifespan):
    total_record[mortgage_term+1,i]=equity[0,i]

for i in range(lifespan):
    total_record[mortgage_term+2,i]=reinvestment[0,i]

for i in range(lifespan):
    total_record[mortgage_term+3,i]=owned_property[0,i]

xaxis=range(0,investment_period+5)

figure(figsize=(15,9))

subplot(221)
title('Outright Properties Owned')
plot(xaxis,owned_property[0,:investment_period+5])
xlabel('Year')
ylabel('Properties Owned')

subplot(222)
title('Debt Level')
plot(xaxis,debt[0,:investment_period+5])
xlabel('Year')
ylabel('Debt')

subplot(223)
title('Equity')
plot(xaxis,equity[0,:investment_period+5])
xlabel('Year')
ylabel('Equity')

subplot(224)
title('Fuck Factor')
plot(xaxis,equity[0,:investment_period+5]-debt[0,:investment_period+5])
xlabel('Year')
ylabel('Level of Fuckedness')

tight_layout()
savefig('sim_output.jpg')

#savetxt('property_records.csv',property_status,delimiter=',')
#savetxt('debt_records.csv',debt,delimiter=',')
#savetxt('owned_property.csv',owned_property,delimiter=',')
#savetxt('equity.csv',equity,delimiter=',')
#savetxt('reinvestment_records.csv',reinvestment,delimiter=',')
savetxt('simulation output.csv',total_record,delimiter=',')

#The results of the analysis are held in the order (property status, debt, equity, reinvestment fund, owned property)

#This writes all the parameters to a text file
file=open("simulation_parameters.txt","w")
file.write("Starting Capital: "+str(starting_capital)+"\n")
file.write("Yearly contribution: "+str(yearly_contribution)+"\n")
file.write("Average House Price: "+str(average_house_price)+"\n")
file.write("Average House Valuation: "+str(average_house_valuation)+"\n")
file.write("Mortgage Term: "+str(mortgage_term)+"\n")
file.write("Interest Rate: "+str(interest_rate)+"\n")
file.write("Investment Period: "+str(investment_period)+"\n")
file.write("Maintenance Fund Goal: "+str(minimum_maintenance_fund)+"\n")
file.write("Monthly Landlords Insurance Contribution: "+str(landlords_insurance)+"\n")
file.write("Monthly Rental Insurance Contribution: "+str(rental_insurance)+"\n")
file.write("Monthly Maintenance Fund Contribution: "+str(maintenance_fund_contribution)+"\n")
file.write("Monthly Management Fees: "+str(management_fees)+"\n")
file.close()

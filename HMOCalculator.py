import streamlit as st
import time

st.image('Wellness.jpg') #welness image
st.title('Wellness Health Insurance Calculator') #title of the proj...
#sidebar
st.sidebar.header("Contact")
st.sidebar.write("Head Office: 9,Jogunomi Street, Gbagada Phase2, Lagos")
st.sidebar.write("Web:https://www.wellnesshealthcare.com.ng/")
st.sidebar.write("Email:info@wellnesshealthcare.com.ng")
print('/n')
st.sidebar.video("Wellness HMO Plan.mp4")

#information to subscriber
st.info("Hi, Good Day, Welcome to Wellness HMO, I am your health insurance friend, kindly allow me to help you calculate your health insurance PAYMENT plan by filling the following information")

st.header("Demographics:")
Name=st.text_input("Enter your FullName",type="default")
Phone_Number=st.text_input("Enter Your PhoneNumber",type="default")
Home_Address=st.text_input("Enter Your Home Address",type="default")
Email_Address=st.text_input("Enter Your Email Address",type="default")
Age_range=st.selectbox("Select Your Age Range:",['Below 10years','10yrs-<18yrs','18yrs-<30yrs','30yrs-<45yrs','45yrs & Above'])
Sex=st.selectbox("Select Your Gender:",['Male','Female'])
Life_style=st.selectbox("Your Life Style?:",['','Drink','Smoke'])
#for drinkers and smokers alone
if Life_style=="Drink":
    Life_style_freq=st.selectbox("How often?:",['Drinks Occassionally','Few Glasses Daily'])
elif Life_style=="Smoke":
    Life_style_freq=st.selectbox("How Often?:",['Smoke Occassionally','Smoke Daily'])
elif Life_style=='':
    Life_style_freq=""

#Continue Demographic
Existing_illness=st.selectbox("Any existing illness?:",['Yes','No'])
Marital_status=st.selectbox('Marital Status:',['Single','Married','Divorced','Separated'])
Choice_of_hosp=st.selectbox('Choice of Hospital/Clinic:',['R-Jolad','Paelon','Premier Specialist','Isalo'])

#for female gender alone
if Sex=="Female":
    last_menstral=st.selectbox("Select Your Last Period:",["",'Last Month',"2months",'3months & Above'])
elif Sex=="Male":
    last_menstral=""

#Benefits
st.header("Health Benefits")
st.info("Please fill in appropriate information which you would prefer to have as your HMO Package")
Ambulance_service=st.selectbox("Would you like Ambulance service?:",['Yes','No'])
Type_of_Care=st.selectbox("Type of Medical Service:",['','Primary','Secondary'])
Specialist_Consult=st.selectbox("Specialist Consult:",['','1-3Specialist','3-6Specialist'])
Diagnostics=st.selectbox("Diagnostics:",['','Primary','Secondary','Advanced'])
immunization=st.selectbox("Immunization Preference:",['','0-5years','Adult'])
Mertanity_care=st.selectbox("Mertanity Choice:",['','Ante-natal','Delivery','Post-Natal','Ante-Natal+Delivery','Ante-Natal+delivery+Post-Natal','Post-Natal+Delivery','Ante-Natal+Post-Natal'])
Delivery_service=st.selectbox("Choice of delivery service:",['Normal','Assisted','Ceaserian Section',''])


#Callculating the Demographics
#Age_range
if Age_range=="Below 10years":
    Age_Point=5
elif Age_range=="10yrs-<18yrs":
    Age_Point=2
elif Age_range=="18yrs-<30yrs":
    Age_Point=4
elif Age_range=="30yrs-<45yrs":
    Age_Point=7
elif Age_range=="45yrs & Above":
    Age_Point=10
else:
    Age_Point=0

#Sex
if Sex=="Male":
    Sex_Point=0
elif Sex=="Female":
    Sex_Point=0

#Life Style
if Life_style=="Drink":
    Life_style_Point=5
elif Life_style=="Smoke":
    Life_style_Point=5
else:
    Life_style_Point=0
#Life_Style_freq
if Life_style_freq=="Drink Occassionally":
    Life_Style_freq_Point=2
elif Life_style_freq=="Few Glasses Daily":
    Life_Style_freq_Point=5
elif Life_style_freq=="Smoke Occassionally":
    Life_Style_freq_Point=2
elif Life_style_freq=="Smoke Daily":
    Life_Style_freq_Point=5
else:
    Life_Style_freq_Point=0

#Existing illness
if Existing_illness=="Yes":
    Existing_illness_Point=10
else:
    Existing_illness_Point=0
#marital Marital_status
if Marital_status=="Single":
    Marital_status_Point=1
elif Marital_status=="Married":
    Marital_status_Point=4
elif Marital_status=="Divorced":
    Marital_status_Point=5
elif Marital_status=="separated":
    Marital_status_Point=3
else:
    Marital_status_Point=0

#Choice of Hospital
if Choice_of_hosp=="R-Jolad":
    Choice_of_hosp_Point=2
elif Choice_of_hosp=="Paelon":
    Choice_of_hosp_Point=8
elif Choice_of_hosp=="premier Specialist":
    Choice_of_hosp_Point=10
elif Choice_of_hosp=="Isalo":
    Choice_of_hosp_Point=5
else:
    Choice_of_hosp_Point=0

#last_menstral
if last_menstral=="Last Month":
    last_menstral_Point=0
elif  last_menstral=="2Months":
    last_menstral_Point=4
elif last_menstral=="3months & above":
    last_menstral_Point=7
elif last_menstral=="":
    last_menstral_Point=0


#lets calculate for Benefits
#Ambulance_service
if Ambulance_service=="Yes":
    Ambulance_service_Point=2
else:
    Ambulance_service_Point=0
#Type_of_Care
if Type_of_Care=="Primary":
    Type_of_Care_Point=5
elif Type_of_Care=="Secondary":
    Type_of_Care_Point=10
else:
    Type_of_Care_Point=0
#Specialist_Consult
if Specialist_Consult=="1-3Specialist":
    Specialist_Consult_Point=5
elif Specialist_Consult=="3-6Specialist":
    Specialist_Consult_Point=10
else:
    Specialist_Consult_Point=0
#Diagnostics
if Diagnostics=="Primary":
    Diagnostics_Point=2
elif Diagnostics=="Secondary":
    Diagnostics_Point=5
elif Diagnostics=="Advanced":
    Diagnostics_Point=10
else:
    Diagnostics_Point=0
#immunization
if immunization=="0-5years":
    immunization_Point=5
elif immunization=="Adult":
    immunization_Point=4
else:
    immunization_Point=0
#Mertanity_care
if Mertanity_care=="Ante-Natal":
    Mertanity_care_Point=2
elif Mertanity_care=="Ante-Natal+Delivery":
    Mertanity_care_Point=5
elif Mertanity_care=="Ante-Natal+Delivery+Post-Natal":
    Mertanity_care_Point=8
elif Mertanity_care=="Delivery+Post-Natal":
    Mertanity_care_Point=5
elif Mertanity_care=="Ante-Natal+Post-Natal":
    Mertanity_care_Point=3
elif Mertanity_care=="delivery":
    Mertanity_care_Point=4
elif Mertanity_care=="Post-Natal":
    Mertanity_care_Point=2
else:
    Mertanity_care_Point=0

#Delivery_service
if Delivery_service=="Normal":
    Delivery_service_Point=4
elif Delivery_service=="Assisted":
    Delivery_service_Point=6
elif Delivery_service=="Ceaserian Section":
    Delivery_service_Point=10
else:
    Delivery_service_Point=0


#Design Calculator button
if st.button("Calculate My health Cost and Plan:"):
    result=Age_Point+Sex_Point+Life_style_Point+Life_Style_freq_Point+Existing_illness_Point+Marital_status_Point+Choice_of_hosp_Point+last_menstral_Point+Ambulance_service_Point+Type_of_Care_Point+Specialist_Consult_Point+Diagnostics_Point+immunization_Point+Mertanity_care_Point+Delivery_service_Point
    result=result*1000
    with st.spinner("Your Payment Loading..."):
        time.sleep(5)
        st.balloons()
    st.success(f"Thank you choosing Wellness HMO, Your Payment is N{result}")
print('/n')
st.write("Would You Like To Pay Now?")
if st.button("Make Payment"):
    st.markdown("Send Your Paymnet to Wellness Account:")
    st.markdown("Bank Name: GTBank")
    st.markdown("Account Number:0234567890")
    st.info("Kindly send your payment evidence to us @ info@wellnesshealthcare.com.ng for your HMO Plan package processing. Our Customer service will reach out to you. THANK YOU!")
st.error("Please fill all information relevant to you")

import streamlit as st
import pickle
import pandas as pd


model = pickle.load(open("C:\\Users\\Rotimi\\Downloads\\model.pkl",'rb'))

st.title('Clients Churn Probability Predictor')
st.sidebar.header('Clients Data')

#creating a function for the values
def user_report():
    REGION = st.sidebar.selectbox('Clients region', ['FATICK', 'DAKAR', 'LOUGA', 'TAMBACOUNDA', 'KAOLACK', 'THIES',
       'SAINT-LOUIS', 'KOLDA', 'KAFFRINE', 'DIOURBEL', 'ZIGUINCHOR', 'MATAM', 'SEDHIOU', 'KEDOUGOU'])
    if(REGION == 'FATICK'):
        REGION = 2,
    elif(REGION == 'DAKAR'):
        REGION = 0,
    elif(REGION == 'LOUGA'):
        REGION = 7,
    elif(REGION == 'TAMBACOUNDA'):
        REGION = 11,
    elif(REGION == 'KAOLACK'):
        REGION = 4,
    elif(REGION == 'THIES'):
        REGION = 12,
    elif(REGION == 'SAINT-LOUIS'):
        REGION = 9,
    elif(REGION == 'KOLDA'):
        REGION = 6,
    elif(REGION == 'KAFFRINE'):
        REGION = 3,
    elif(REGION == 'DIOURBEL'):
        REGION = 1,
    elif(REGION == 'ZIGUINCHOR'):
        REGION = 13,
    elif(REGION == 'MATAM'):
        REGION = 8,
    elif(REGION == 'SEDHIOU'):
        REGION = 10,
    else:
        REGION = 5
    TENURE = st.sidebar.selectbox('Please select Tenure', ('K > 24 month', 'I 18-21 month', 'G 12-15 month', 'H 15-18 month',
       'J 21-24 month', 'F 9-12 month', 'D 3-6 month', 'E 6-9 month'))
    if(TENURE == 'K > 24 month'):
        TENURE = 7,
    elif(TENURE == 'I 18-21 month'):
        TENURE = 5,
    elif (TENURE == 'G 12-15 month'):
        TENURE = 3,
    elif (TENURE == 'H 15-18 month'):
        TENURE = 4,
    elif (TENURE == 'J 21-24 month'):
        TENURE = 6,
    elif (TENURE == 'F 9-12 month'):
        TENURE = 2,
    elif (TENURE == 'D 3-6 month'):
        TENURE = 0,
    else:
        TENURE = 1
    MONTANT = st.sidebar.number_input('Enter top-up amount')
    FREQUENCE_RECH = st.sidebar.number_input('Enter number of times client refilled')
    REVENUE = st.sidebar.number_input('Enter clients monthly income')
    ARPU_SEGMENT = st.sidebar.number_input('Enter clients income in 90 days')
    FREQUENCE = st.sidebar.number_input('Enter number of times the client made an income')
    ON_NET = st.sidebar.number_input('Enter number of calls made on Expresso network')
    ORANGE = st.sidebar.number_input('Enter number of calls to Orange network')
    TIGO = st.sidebar.number_input('Enter number of calls to Tigo network')
    REGULARITY = st.sidebar.number_input('Enter number of times client is active for 90 days')
    FREQ_TOP_PACK = st.sidebar.number_input('Enter number of times client activated top pack packages')

    # creating a dictionary of the values
    user_report_data = {
        'REGION': REGION,
        'TENURE': TENURE,
        'MONTANT': MONTANT,
        'FREQUENCE_RECH': FREQUENCE_RECH,
        'REVENUE': REVENUE,
        'ARPU_SEGMENT': ARPU_SEGMENT,
        'FREQUENCE': FREQUENCE,
        'ON_NET': ON_NET,
        'ORANGE': ORANGE,
        'TIGO': TIGO,
        'REGULARITY': REGULARITY,
        'FREQ_TOP_PACK': FREQ_TOP_PACK
    }
    report_data = pd.DataFrame(user_report_data, index = [0])
    return report_data
user_data = user_report()

st.subheader('Client data summary')
st.write(user_data)

Churn = model.predict(user_data)
if (st.sidebar.button('Calculate Churn Probability')):
    st.text("Clients churn probability is {}.".format(Churn))


st.subheader('Churn Probability')
if(Churn == 1):
    st.warning('The client will most likely stop his/her subscription')
else:
    st.success('The client will continue with his/her subscription')
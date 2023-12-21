import streamlit as st
import pandas as pd
import pickle
st.title('Laptop Prediction')
st.sidebar.header('Details about laptop information')
def input():
    
    comp=st.sidebar.selectbox('Company',('Dell','Lenovo','HP','Asus','Acer','MSI',         
    'Toshiba','Apple','Samsung','Razer','Mediacom','Microsoft','Xiaomi','Vero',           
    'Chuwi','Google','Fujitsu','LG','Huawei'))
    typ=st.sidebar.selectbox('TypeName',('Notebook','Gaming','Ultrabook','2 in 1 Convertible'    
    ,'Workstation','Netbook'))
    rm=st.sidebar.selectbox("Ram",(8,4,16,6,12,32,2,24,64))
    ts=st.sidebar.selectbox("TS",(0,1))
    ips=st.sidebar.selectbox("Ips",(0,1))
    scr=st.sidebar.number_input("Scrnsize")
    wg=st.sidebar.number_input("Weight")   
    pp=st.sidebar.number_input("ppi")    
    hd=st.sidebar.selectbox("HDD",(0,1000,500,2000,32,128))
    sd=st.sidebar.selectbox("SSD",(256,0,128,512,1000,32,180,16,64,1024,768,240,8))
    os=st.sidebar.selectbox("Os",('Windows','Others','Mac'))    
    cp=st.sidebar.selectbox("Cpu_brand",('Intel Core i7','Intel Core i5','Other Intel Processor','Intel Core i3','AMD Processor'))
    gp=st.sidebar.selectbox("Gpu_brand",('Intel','Nvidia','AMD')) 
    
    
    
    data={'Company': comp,
     'TypeName': typ,
     'Ram': rm,
     'Weight': wg,
     'TS': ts,
     'Ips': ips,
     'Ppi': pp,
     'Cpu_brand': cp,
     'HDD': hd,
     'SSD': sd,
     'Gpu_brand':gp,
     'Os': os,
     'Scrnsize': scr,
     }
    
    
    features = pd.DataFrame(data,index = [0])
    return features 

df=input()
st.subheader("Laptop info")
st.write(df)

with open('final_model.sav',mode = 'rb') as f:
    model = pickle.load(f)
Prediction=model.predict(df)
st.subheader("Laptop price")
st.write(Prediction[0])
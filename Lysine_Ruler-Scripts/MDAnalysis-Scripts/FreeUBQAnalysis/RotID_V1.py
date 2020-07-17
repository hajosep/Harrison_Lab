
# coding: utf-8

# In[ ]:


import pandas as pd

# In[ ]:
def PClassy(Val):
    if(Val < -170):
        return -18
    elif(Val < -160):
        return -17
    elif(Val < -150):
        return -16
    elif(Val < -140):
        return -15
    elif(Val < -130):
        return -14
    elif(Val < -120):
        return -13
    elif(Val < -110):
        return -12
    elif(Val < -100):
        return -11
    elif(Val < -90):
        return -10
    elif(Val < -80):
        return -9
    elif(Val < -70):
        return -8
    elif(Val < -60):
        return -7
    elif(Val < -50):
        return -6
    elif(Val < -40):
        return -5
    elif(Val < -30):
        return -4
    elif(Val < -20):
        return -3
    elif(Val < -10):
        return -2
    elif(Val < 0):
        return -1
    elif(Val < 10):
        return 1
    elif(Val < 20):
        return 2
    elif(Val < 30):
        return 3
    elif(Val < 40):
        return 4
    elif(Val < 50):
        return 5
    elif(Val < 60):
        return 6
    elif(Val < 70):
        return 7
    elif(Val < 80):
        return 8
    elif(Val < 90):
        return 9
    elif(Val < 100):
        return 10
    elif(Val < 110):
        return 11
    elif(Val < 120):
        return 12
    elif(Val < 130):
        return 13
    elif(Val < 140):
        return 14
    elif(Val < 150):
        return 15
    elif(Val < 160):
        return 16
    elif(Val < 170):
        return 17
    elif(Val <= 180):
        return 18

def ChiClassy(Val):
    if(Val <= -120 or Val >= 120):
        return 0
    if(Val < 0 and Val > -120):
        return -1
    if(Val >= 0 and Val < 120 ):
        return 1


def MutRoundup(DF):
    ChangeDF = pd.DataFrame()
    for i in range(0,len(DF)):
        PhiC = PClassy(DF.at[i,'Phi'])
        PsiC = PClassy(DF.at[i,'Psi'])
        C1C = ChiClassy(DF.at[i,'Chi1'])
        C2C = ChiClassy(DF.at[i,'Chi2'])
        C3C = ChiClassy(DF.at[i,'Chi3'])
        C4C = ChiClassy(DF.at[i,'Chi4'])
        C5C = ChiClassy(DF.at[i,'Chi5'])
        ChangeDF.at[i,'Frame'] = str(i)
        ChangeDF.at[i,'Array'] = [PhiC,PsiC,C1C,C2C,C3C,C4C,C5C]
        if(i % 5000 == 0):
            print(i)
    return ChangeDF

def NatRoundup(DF):
    ChangeDF = pd.DataFrame()
    for i in range(0,len(DF)):
        PhiC = PClassy(DF.at[i,'Phi'])
        PsiC = PClassy(DF.at[i,'Psi'])
        C1C = ChiClassy(DF.at[i,'Chi1'])
        C2C = ChiClassy(DF.at[i,'Chi2'])
        C3C = ChiClassy(DF.at[i,'Chi3'])
        C4C = ChiClassy(DF.at[i,'Chi4'])
        ChangeDF.at[i,'Frame'] = str(i)
        ChangeDF.at[i,'Array'] = str([PhiC,PsiC,C1C,C2C,C3C,C4C])
        if(i % 5000 == 0):
            print(i)
    return ChangeDF

# K63Mut = pd.read_csv('K63-ChargedAngles.csv', index_col = 0)
# K63Nat = pd.read_csv('K63NativeAngles.csv', index_col = 0)


# K63MutRotID = NatRoundup(K63Mut)
# K63MutRotID.to_csv('K63Mut-R1-Changes.csv')
# K63NatRotID = NatRoundup(K63Nat)
# K63NatRotID.to_csv('K63Nat-R1-Changes.csv')

DF1 = pd.read_csv('K63NativeAngles.csv', index_col = 0)
DF2 = pd.read_csv('K63NativeAngles-V2.csv', index_col = 0)

NatRoundup(DF1).to_csv('K63-Nat-R1-RotBin.csv')
NatRoundup(DF2).to_csv('K63-Nat-R2-RotBin.csv')
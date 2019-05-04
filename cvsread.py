import csv
import math

def fun(str):
    if str=='':
        return 0
    else:
        return int(str)
def fun2(str):
    if str=='':
        return 0
    else:
        return float(str)

def linear_reg(x, y):
    n = len(x)
    m_x, m_y = float(sum(x))/n, float(sum(y))/n
    SS_xy = sum(y[i]*x[i] for i in range(n)) - n*m_y*m_x
    SS_xx = sum(x[i]*x[i] for i in range(n)) - n*m_x*m_x
    b_1 = SS_xy / SS_xx
    """b_0 = m_y - b_1*m_x"""
    return b_1

def chi_square(M,T):
    m=float(sum(M))
    t=float(sum(T))
    return sum(pow((M[i]-m*T[i]/t),2)/(m*T[i]/t)+pow((T[i]-M[i]-(t-m)*T[i]/t),2)/((t-m)*T[i]/t) for i in range(len(M)))

with open('/Users/xinghuagao/Documents/NYPD_Motor_Vehicle_Collisions.csv') as csv_file:
    r_lat=6357
    r_long=6378
    csv_reader = csv.reader(csv_file, delimiter=',')
    line=1
    end18=0
    end17=0
    end16=0
    end15=0
    end14=0
    end13=0
    end12=0
    for row in csv_reader:
        if not end18 and row[0]=="12/31/2018":
            end18=line
        if not end17 and row[0]=="12/31/2017":
             end17=line
        if not end16 and row[0]=="12/31/2016":
             end16=line
        if not end15 and row[0]=="12/31/2015":
             end15=line
        if not end14 and row[0]=="12/31/2014":
             end14=line
        if not end13 and row[0]=="12/31/2013":
             end13=line
        if not end12 and row[0]=="12/31/2012":
             end12=line
        line+=1

    csv_file.seek(0)

    inj = 0
    inj18=0
    inj17=0
    inj16=0
    inj15=0
    inj14=0
    inj13=0
    cyc16=0
    line=1
    bro16=0
    dict={}
    multi17=[0]*12
    collision17=[0]*12
    alc_inv17={'BRONX':0, 'BROOKLYN':0, 'MANHATTAN':0, 'QUEENS':0, 'STATEN ISLAND':0}
    location17={}
    std17={}
    polulation={'BRONX':float(1471160), 'BROOKLYN':float(2648771), 'MANHATTAN':float(1664727), 'QUEENS':float(2358582), 'STATEN ISLAND':float(479458)}
    for row in csv_reader:
        if line>=end18:
            inj+=fun(row[10])+fun(row[11])
        if line>=end18 and line<end17:
            inj18+=fun(row[10])+fun(row[11])
        if line>=end17 and line<end16:
            inj17+=fun(row[10])+fun(row[11])
            collision17[int(row[0][0:2])-1]+=1
            if 'Alcohol' in row[18]+row[19]+row[20]+row[21]+row[22] and bool(row[2]):
                alc_inv17[row[2]]+=1
            if int(bool(row[18]))+int(bool(row[19]))+int(bool(row[20]))+int(bool(row[21]))+int(bool(row[22]))>2:
                multi17[int(row[0][0:2])-1]+=1
            if 40<fun2(row[4])<46 and -80<fun2(row[5])<-71:
                if row[3] in location17:
                    location17[row[3]][0]+=fun2(row[4])
                    location17[row[3]][1]+=fun2(row[5])
                    location17[row[3]][2]+=1
                else:
                    location17[row[3]]=[fun2(row[4]),fun2(row[5]),1]
        if line>=end16 and line<end15:
            inj16+=fun(row[10])+fun(row[11])
            cyc16+=fun(row[14])+fun(row[15])
            if row[2]=='BROOKLYN':
                bro16+=fun(row[10])+fun(row[11])
            vehicle=int(bool(row[18]))+int(bool(row[19]))+int(bool(row[20]))+int(bool(row[21]))+int(bool(row[22]))
            if row[3] in dict:
                dict[row[3]]+=vehicle
            else:
                dict[row[3]]=vehicle
        if line>=end15 and line<end14:
            inj15+=fun(row[10])+fun(row[11])
        if line>=end14 and line<end13:
            inj14+=fun(row[10])+fun(row[11])
        if line>=end13 and line<end12:
            inj13+=fun(row[10])+fun(row[11])
        line+=1

    for i in location17:
        location17[i][0]=location17[i][0]/location17[i][2]
        location17[i][1]=location17[i][1]/location17[i][2]

    csv_file.seek(0)
    line=1
    for row in csv_reader:
        if line>=end16:
            break
        if line>=end17 and 40<fun2(row[4])<46 and -80<fun2(row[5])<-71:
            if row[3] in std17 and location17[row[3]][2]>999:
                std17[row[3]][0]+=pow(fun2(row[4])-location17[row[3]][0],2)
                std17[row[3]][1]+=pow(fun2(row[5])-location17[row[3]][1],2)
            elif location17[row[3]][2]>999:
                std17[row[3]]=[pow(fun2(row[4])-location17[row[3]][0],2),pow(fun2(row[5])-location17[row[3]][1],2)]
        line+=1
    for zip in std17:
        std17[zip][0]=math.sqrt(std17[zip][0]/(location17[zip][2]-1))
        std17[zip][1]=math.sqrt(std17[zip][1]/(location17[zip][2]-1))

    print(inj)
    print(float(cyc16)/inj16)
    print(float(bro16)/inj16)
    y=[inj13,inj14,inj15,inj16,inj17,inj18]
    print(linear_reg(range(len(y)),y))
    print(max(dict[i] for i in dict if bool(i)))
    print(max(alc_inv17[i]/polulation[i] for i in alc_inv17))
    print(chi_square([multi17[0],multi17[4]],[collision17[0],collision17[4]]))
    print(max(location17[zip][2]/std17[zip][0]/std17[zip][1]/math.pi/r_long/r_lat for zip in std17 if bool(zip)))
    print(location17)
    print(std17)

#print(dict)
#print(alc_inv17)
    #print(std17)
    #print(location17)

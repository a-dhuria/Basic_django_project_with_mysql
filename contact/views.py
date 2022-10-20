from django.shortcuts import render
import mysql.connector as sql
n=''
em=''
pb=''
# Create your views here.
def contact(request):
    global n,em,pb
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root",database='site')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                n=value
            if key=="email":
                em=value
            if key=="problem":
                pb=value
        
        c="insert into users Values('{}','{}','{}')".format(n,em,pb)
        cursor.execute(c)
        m.commit()

    return render(request,'contact.html')

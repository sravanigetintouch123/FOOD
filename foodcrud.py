#CRUD Operations on variety of food
class food:
    def __init__(self,a=0,b=0,c=0,d=0,e=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
    def display(self):
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
    def update(self,a,b,c,d,e):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
    def __del__(self):
        pass
l=[]
veg=["vegbiriyani","schezwanfriedrice","vegfriedrice","butternaun","meals"]
nonveg=["chickenbiriyani","chickenfriedrice","dumbiriyani","chicken","lolipops","wings"]
ice=["venella","chocolate","butterscotch","strawberry"]
drinks=["pepsi","cococola","sprite","thumbsup","7up"]
list1=[]
for i in veg:
    list1.append(i)
for i in nonveg:
    list1.append(i)
for i in ice:
    list1.append(i)
for i in drinks:
    list1.append(i)
while(1):
    print("enter 1 to order food")
    print("enter 2 to display items")
    print("enter 3 to change the order")
    print("enter 4 to cancel")
    print("enter 5 to exit")
    x=int(input())
    if x==1:
        print("enter the details for making your order")
        a=input("name:")
        b=input("item:")
        if b not in list1:
            print("-------NO ITEM-----")
            b=0
        c=input("item:")
        if c not in list1:
            print("-------NO ITEM-----")
            c=0
        d=input("item:")
        if d not in list1:
            print("-------NO ITEM-----")
            d=0
        e=input("item:")
        if e not in list1:
            print("-------NO ITEM-----")
            e=0
        s=food(a,b,c,d,e)
        l.append(s)
    if x==2:
        print("enter 6 to display available the veg items")
        print("enter 7 to display available the non-veg items")
        print("enter 8 to display drinks")
        print("enter 9 to display ice creams")
        print("enter 10 to dislpay your ordered items")
        h=int(input("enter a number"))
        if h==6:
            for i in veg:
                print(i)
        if h==7:
            for i in nonveg:
                print(i)
        if h==8:
            for i in drinks:
                print(i)
        if h==9:
            for i in ice:
                print(i)
        if h==10:
            if(len(l)==0):
                print("NO ORDERS!!!!!")
                break
            p=input("enter your name")
            for obj in l:
                if obj.a==p:
                    print(obj.a)
                    print(obj.b)
                    print(obj.c)
                    print(obj.d)
                    print(obj.e)              
                else:
                    pass
    if x==3:
        if(len(l)==0):
            print("NO ORDERS!!!!!")
            break
        q=input("yor name:")
        b=input("item:")
        c=input("item:")
        d=input("item:")
        e=input("item:")
        for obj in l:
            if obj.a==q:
                l.remove(obj)
                print("modified and previous details are deleted")
                del obj
            else:
                pass          
            s=food(q,b,c,d,e)
            l.append(s) 
    if x==4:
        if(len(l)==0):
            print("NO ORDERS!!!")
            break
        r=input("enter your name to cancel the order")
        for obj in l:
            if obj.a==r:
                print(obj.a,"order is DELETED")
                l.remove(obj)
                del obj
            
            else:
                pass
    if x==5:
        break
print("Pizza Categories : \n1.Normal\n2.Deluxe\n Enter your Choice [1 or 2]:")
n=int(input())
bill=0.0
if n == 1 :
    print("Pizza Types :\n1.Veg\n2.Non veg\n Enter your Choice[1 or 2]:")
    m=int(input())
    if m == 1 :
        bill+=300
    elif m==2 :
        bill+=400
if n == 2 :
    print("Pizza Types :\n1.Veg\n2.Non veg\n Enter your Choice[1 or 2]:")
    m=int(input())
    if m == 1 :
        bill+=600
    elif m==2 :
        bill+=800
bp=bill
print("Extra Cheese? [1.Yes or 2.NO]:")
k=int(input())
if k==1:
    bill+=100
print("Extra Topping? [1.Yes or 2.NO]:")
l=int(input())
if l==1:
    bill+=100
print("Do you want Water Bottles? [1.Yes or 2.NO]:")
m=int(input())
if m==1:
    print("How many bottles?:")
    n=int(input())
    b=n*20
    bill+=m*20
print("Do you want Ketchup? [1.Yes or 2.NO]: ")
ke=int(input())
if ke==1:
    print("How many packets?:")
    n=int(input())
    s=n*5
    bill += n*5
print("Do you want Soft Driknks? [1.Yes or 2.NO]: ")
sf=int(input())
if sf==1:
    print("How many drinks?:")
    n=int(input())
    l=n*75
    bill+=n*75
print("Is it a Take Away? [1.Yes or 2.NO]: ")
ta=int(input())
if ta==1:
    bill+=20
print("-----------------------")
print("*****Pizza Bill Generator******")
print("-----------------------")
print(f"Base price :{bp}")
if k==1:
    print("extra cheese :100")
if l==1:
     print("extra toppings :100")
if m==1:
     print(f"water bottle :{b}")
if ke==1:
     print(f"ketchup :{s} ")
if sf==1:
     print(f"soft drinks :{l} ")
if ta==1:
     print("take away: 20")
print("-----------------------------")
print(f"Total cost={bill}")
g=bill*0.18
print(f"GST charges ={g}")
tot=g+bill
print("-----------------------------")
print(f"Network amount ={tot}")

##Q:  In a store when a person buys 3 toffees he will get 1 extra toffee as a gift, when he shows the wrappers.
        ##then how many total toffees will he get? if he buys 100 toffees?

tofee=100
wrapper=0
count=0
while tofee>0:
    count+=tofee
    wrapper+=tofee
    tofee=wrapper//3
    wrapper%=3
count+=tofee
print(count)
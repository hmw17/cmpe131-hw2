def sort_list(mylist):
    n=len(mylist)
    i=0
    while(i<n):
        j=0
        while(j<n-i-1):
            temp=0
            if mylist[j]>mylist[j+1]:
                temp=mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp
            j=j+1
        i=i+1
    return mylist

def main():
    mylist=[1, 8, 3, 9]
    sort_list(mylist)
    print(mylist)
main()

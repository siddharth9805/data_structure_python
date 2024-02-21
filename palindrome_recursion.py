def is_pal(n:str,length:int,start:int):
    if length-1==start:
        return True
    elif n[start]!=n[length-1] :
        return False
    else:
        return is_pal(n,length-1,start+1)
def main():
    k=str(input("Enter the string to check the plaindrome :"))
    if is_pal(k,len(k),0):
        print("This is Palindrome")
    else:
        print("This is not palindrome")

if __name__=="__main__":
    main()
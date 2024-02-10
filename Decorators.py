def getval():
    return float(input("Enter Any Number:"))

def ashish(getval):
    def square():     #inner function
        n=getval()
        res=n**2
        return n,res   #Inner function return result
    return square
def sumanth(kvr):
    def cube():
        n=getval()
        res=n**3
        return n,res
    return cube


#mainprogram
sq=ashish(getval)
n,res=sq()
print("Square ({})={}".format(n,res))
print("================================")
cb=sumanth(getval)
n,cres=cb()
print("Cube ({})={}".format(n,cres))
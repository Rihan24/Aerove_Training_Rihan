class Complex:
    def __init__(self,x,y):                            #constructor
        self.x=x
        self.y=y
        
    def display(self):                                 #prints the complex number
        if self.y<0:
            print(self.x,self.y,"i")
        else:
            print(self.x,"+",self.y,"i")
    
    def add(self,a):                                    #returns sum of complex numbers as an object
        return Complex(self.x+a.x,self.y+a.y)
    def sub(self,a):                                    #returns difference of complex numbers as an object
        return Complex(self.x-a.x,self.y-a.y)
    def mul(self,a):                                    #returns product of complex numbers as an object
        return Complex(self.x*a.x -self.y*a.y,self.x*a.y +self.y*a.x)
    def modulus(self):                                  #prints the modulus of comlex number
        print(((pow(self.x,2)+pow(self.y,2)))**0.5)
    def conjugate(self):                                #returns the conjugate complex number as an object
        return Complex(self.x,-self.y)
    def inverse(self):                                  #returns the inverse of complex number as an object
        mod_2=(pow(self.x,2)+pow(self.y,2))
        return Complex((self.conjugate().x)/mod_2,(self.conjugate().y)/mod_2)


        
    
l=Complex(1,2)
l.display()                         #print complex l
l.modulus()                         #print modulus of l

m=Complex(2,-3)
m.display()                         #print comlex m
m.conjugate().display()             #print conjugate m
c=m.add(l)
c.display()                         #print l+m
d=m.sub(l)
d.display()                         #print m-l
e=m.mul(l)
e.display()                         #print m*l
f=l.inverse()
f.display()                         #print inverse of l



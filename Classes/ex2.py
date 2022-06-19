from regex import W


class MyCalc:

    def simple_interest(self,p,r,t):
        return p*r*t/100

    def compound_interest(self,p,r,t):
        return p*(1+(r/100))**t

    def area_of_triangle(self,b,h):
        return 0.5*b*h

    def area_of_circle(self,r):
        return 3.14*r**2

    def area_of_rectangle(self,1,w):
        return 1*W

    if __name__ == '__main__':
        c = MyCalc()
        print(c.simple_interest(100,10,2))
        print(c.compound_interest(100,10,2))                    
class Utils:

    @staticmethod
    def roundEqual(a,b):

        if abs(a-b)<=0.001:
            return True
        else:
            return False

    @staticmethod
    def precion2places(num):
        a=int(num*100)
        x=a/100
        return x

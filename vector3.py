'''
vectorClass.py

Jens Hansen
jensvhansen.com

version: 1.2

update notes:
- now returns a new vector object where suitable for clearner coding when using the vector class
- better commenting


sources: 
reason to use tuple 
http://stackoverflow.com/questions/68630/are-tuples-more-efficient-than-lists-in-python

'''
from math import acos, sin, sqrt


class vector3(object):
    
    
    def __init__(self, *args):

        """
        Represents a 3D vector with common vector operations.

        The vector object can be initialized by:
            - list/tuple with 3 indices.
            - 3 separate values.
            - if no values are entered a object with 
                the values of 0,0,0 is created. 
        """
        if   len(args) == 1:
            try: 
                self._v = (args[0][0], args[0][1],args[0][2])
            except:
                return "typeError"

        elif len(args) == 3:
            try:
                self._v = (args[0], args[1], args[2])
            except:
                return "typeError"

        elif not args:
            self._v = (0.0, 0.0, 0.0)
        else:
            raise TypeError()


    def __repr__(self):
        return ("Vector3({x}, {y}, {z})").format(x = self._v[0], y = self._v[1], z = self._v[2]) 
    
    def __str__(self):
        return ("({x}, {y}, {z})").format(x = self._v[0], y = self._v[1], z = self._v[2])
    
    # add
    def __add__(self, other):
        """ Addition
        checks what object the vector is added with 
        and runs the correct operation.
        """
        if isinstance(other, vector3):
            # adds corresponding indices.
            return vector3([i + j for i, j in zip(self._v, other._v)])
            
        elif isinstance(other, int) or isinstance(other, float):
            # adds all original indices with the inputed scalar.
            return vector3([i + other for i in self._v])
        
        elif isinstance(other, list) or isinstance(other, tuple) and len(other) == 3:
            # adds corresponding indices.
            return vector3([i + j for i, j in zip(self._v, other)])
        
        else:
            raise TypeError("Vector3 can only be added with vector3, float/int value or list/tuple with 3 values.")
        
    # subtract
    def __sub__(self, other):
        """ Subtraction
        checks what object the vector is added with 
        and runs the correct operation.
        """
        if isinstance(other, vector3):
            # subtracts corresponding indices.
            return vector3([i - j for i, j in zip(self._v, other._v)])
            
        elif isinstance(other, int) or isinstance(other, float):
            # subtracts all original indices with the inputed scalar.
            return vector3([i - other for i in self._v])

        elif isinstance(other, list) or isinstance(other, tuple) and len(other) == 3:
            # subtracts corresponding indices.
            return vector3([i - j for i, j in zip(self._v, other)])
        
        else:
            raise TypeError("Vector3 can only be subtracted with vector3, float/int value or list/tuple with 3 values.")
   
    # multiply
    def __mul__(self, other):
        """ Multiply
        Multiplies a scalar with the indices of the vector.
        """
        if isinstance(other, int) or isinstance(other, float):
            return vector3([i * other for i in self._v])
        else:
            raise ValueError()       
    
    # divide
    def __div__(self,other):
        """ Divide
        Divides a scalar with the indices of the vector.
        """
        if isinstance(other, int) or isinstance(other, float):
            return vector3([i / other for i in self._v])
        else:
            raise ValueError() 
    
    def get(self):
        """return the values of the vector."""
        return self._v[0], self._v[1], self._v[2]
    
    def getString(self):
        """  
        returns a string of the vector
        """
        return "{x:4f} {y:4f} {z:4f} ".format(x = self._v[0], y = self._v[1], z = self._v[2])
    
    ############ X
    @property
    def x(self):        # get x
        """return the x value of the vector"""
        return self._v[0]
    
    ############ Y
    @property
    def y(self):        # get y
        """return the z value of the vector"""
        return self._v[1]
    
    ############ Z
    @property
    def z(self):        # get z
        """return the z value of the vector"""
        return self._v[2]

    # magnitude
    def mag(self):
        """return the magnitude(length) of a vector."""
        return sqrt(sum([axis**2 for axis in self._v]))
    
    # unit
    def unit(self):
        """return the unit vector of self"""
        magConst = self.mag()
        return vector3([axis / magConst for axis in self._v])
    
    # dot product 
    def dotp(self, other):
        """return the dot product of two vectors."""
        return sum(tuple(a * b for a, b in zip(self._v, other._v)))
    
    # dot angle 
    def dota(self, other):
        """return the angle between two vectors."""
        
        # check if the input vectors are unit vectors
        if round(self.mag(),5) == 1: a = self
        else:
            a = self.unit()
            
        if round(other.mag(),5) == 1: b = other
        else: 
            b = other.unit()
        
        angle = self.clamp(-1, 1, (self.dotp(other) / (a.mag()*b.mag())))
        
        return acos(angle)

    # cross product 
    def crossp(self, other):
        """calculated the cros sproduct of self and other vector
            x = v1.x * v2.z - v1.z * v2.y
            y = v1.z * v2.x - v1.x * v2.z
            z = v1.x * v2.y - v1.y * v2.x
        """
        a = self
        b = other
        return vector3([a.y * b.z - a.z * b.y, 
                                a.z * b.x - a.x * b.z, 
                                a.x * b.y - a.y * b.x])
    
    # cross magnitude
    def crossm(self, other):
        """return the magnitude(lenght) of the cross product of two vectors.
            magnitude v1 * magnitude v2 * sine( dotproduct v1, v2)
        
        """   
        return (self.mag() * other.mag()) * sin(self.dota(other))

    # area of a triangle defined by two vectors
    def tria(self, other):
        """returns half the area(=triangle) of the parallelogram formed by two vectors."""
        return self.crossm(other) / 2
    
    def clamp(self, lowvalue, highvalue, driver):
        if      driver < lowvalue:      driver = lowvalue
        elif    driver > highvalue:     driver = highvalue
        return driver


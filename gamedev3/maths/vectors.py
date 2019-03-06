import numpy as np

from .common import Vector

class Vec2(Vector):

    def __init__(self, values):
        super().__init__(values, 2)

    ########################################
    #   Returns New Vectors. Override These
    ########################################

    def cross_product(self, vector):
        return Vec2(self._cross(vector))

    def hadamard_product(self, vector):
        assert isinstance(vector, Vec2), "vector must be an instance of Vec2."
        return Vec2(self._hadamard(vector))

    def inverse(self):
        return Vec2(self._inverse())

    def transform(self, matrix):
        return Vec2(self._transform(matrix))

    def normalize(self):
        return Vec2(self._normalize())

    def divide(self, vector):
        assert isinstance(vector, Vec2), "vector must be an instance of Vec2."
        return Vec2(self._divide(vector))

    def add(self, vector):
        assert isinstance(vector, Vec2), "vector must be an instance of Vec2."
        return Vec2(self._add(vector))

    def subtract(self, vector):
        assert isinstance(vector, Vec2), "vector must be an instance of Vec2."
        return Vec2(self._subtract(vector))

    def scalar(self, scalar):
        return Vec2(self._scalar(scalar))

    def __repr__(self):
        return "<Vec2 %s>"%self.value

    @property
    def x(self):
        return self.value[0]
    @property
    def y(self):
        return self.value[1]

    @classmethod
    def ZERO(cls):
        return Vec2([0,0])
    @classmethod
    def SCALAR(cls, scalar):
        return Vec2([scalar, scalar])
    @classmethod
    def VEC3(cls, vec3):
        assert isinstance(vec3, Vec3), "VEC3 requires a Vec3 instance"
        return Vec2([vec3.value[0], vec3.value[1]])
    @classmethod
    def XAXIS(cls):
        return Vec2([1,0])
    @classmethod
    def YAXIS(cls):
        return Vec2([0,1])

    @classmethod
    def DIMENSIONS(cls):
        return 2

class Vec3(Vector):

    def __init__(self, values):
        super().__init__(values, 3)

    ########################################
    #   Returns New Vectors. Override These
    ########################################

    def cross_product(self, vector):
        assert isinstance(vector, Vec3), "vector must be an instance of Vec3."
        return Vec3(self._cross(vector))

    def hadamard_product(self, vector):
        assert isinstance(vector, Vec3), "vector must be an instance of Vec3."
        return Vec3(self._hadamard(vector))

    def inverse(self):
        return Vec3(self._inverse())

    def transform(self, matrix):
        return Vec3(self._transform(matrix))

    def normalize(self):
        return Vec3(self._normalize())

    def divide(self, vector):
        assert isinstance(vector, Vec3), "vector must be an instance of Vec3."
        return Vec3(self._divide(vector))

    def add(self, vector):
        assert isinstance(vector, Vec3), "vector must be an instance of Vec3."
        return Vec3(self._add(vector))

    def subtract(self, vector):
        assert isinstance(vector, Vec3), "vector must be an instance of Vec3."
        return Vec3(self._subtract(vector))

    def scalar(self, scalar):
        return Vec3(self._scalar(scalar))

    def __repr__(self):
        return "<Vec3 %s>"%self.value

    @property
    def x(self):
        return self.value[0]
    @property
    def y(self):
        return self.value[1]
    @property
    def z(self):
        return self.value[2]

    @classmethod
    def SCALAR(cls, scalar):
        return Vec3([scalar, scalar, scalar])
    @classmethod
    def VEC2(cls, vec2):
        assert isinstance(vec2, Vec2), "VEC2 requires a Vec2 instance"
        return Vec3([vec2.value[0], vec2.value[1], 0.0])
    @classmethod
    def VEC4(cls, vec4):
        assert isinstance(vec4, Vec4), "VEC4 requires a Vec4 instance"
        return Vec3([vec4.value[0], vec4.value[1], vec4.value[2]])
    @classmethod
    def ZERO(cls):
        return Vec3([0,0,0])
    @classmethod
    def UP(cls):
        return Vec3([0,1,0])
    @classmethod
    def DOWN(cls):
        return Vec3([0,-1,0])
    @classmethod
    def LEFT(cls):
        return Vec3([-1,0,0])
    @classmethod
    def RIGHT(cls):
        return Vec3([1,0,0])
    @classmethod
    def XAXIS(cls):
        return Vec3([1,0,0])
    @classmethod
    def YAXIS(cls):
        return Vec3([0,1,0])
    @classmethod
    def ZAXIS(cls):
        return Vec3([0,0,1])

    @classmethod
    def DIMENSIONS(cls):
        return 3

class Vec4(Vector):

    def __init__(self, values):
        super().__init__(values, 4)

    ########################################
    #   Returns New Vectors. Override These
    ########################################

    def cross_product(self, vector):
        return Vec4(self._cross(vector))

    def hadamard_product(self, vector):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Vec4(self._hadamard(vector))

    def inverse(self):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Vec4(self._inverse())

    def transform(self, matrix):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Vec4(self._transform(matrix))

    def normalize(self):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Vec4(self._normalize())

    def divide(self, vector):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Vec4(self._divide(vector))

    def add(self, vector):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Vec4(self._add(vector))

    def subtract(self, vector):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Vec4(self._subtract(vector))

    def scalar(self, scalar):
        return Vec4(self._scalar(scalar))

    def __repr__(self):
        return "<Vec4 %s>"%self.value

    @property
    def x(self):
        return self.value[0]
    @property
    def y(self):
        return self.value[1]
    @property
    def z(self):
        return self.value[2]
    @property
    def w(self):
        return self.value[3]

    @classmethod
    def ZERO(cls):
        return Vec4([0,0,0,0])
    @classmethod
    def SCALAR(cls, scalar):
        return Vec4([scalar, scalar, scalar, scalar])
    @classmethod
    def VEC3(cls, vec3):
        assert isinstance(vec3, Vec3), "VEC3 requires a Vec3 instance"
        return Vec4([vec3.value[0], vec3.value[1], vec3.value[2], 0.0])

    @classmethod
    def DIMENSIONS(cls):
        return 4

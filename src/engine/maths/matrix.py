import numpy as np
from math import radians, cos, sin

from .common import Matrix
from .vectors import Vec4, Vec3

class Mat4(Matrix):
    def __init__(self, values):
        super().__init__(values, (4,4))

    ########################################
    #   Returns New Matricies. Override These
    ########################################

    def add(self, matrix):
        assert isinstance(matrix, Mat4), "matrix must be an instance of Mat4."
        return Mat4(self._add(matrix))

    def subtract(self, matrix):
        assert isinstance(matrix, Mat4), "matrix must be an instance of Mat4."
        return Mat4(self._subtract(matrix))

    def scalar(self, scalar):
        return Mat4(self._scalar(scalar))

    def multiply(self, matrix):
        assert isinstance(matrix, Mat4), "matrix must be an instance of Mat4."
        return Mat4(self._multiply(matrix))

    def column(self, key):
        return Vec4(self._column(key))

    def set_column(self, key, vector):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Mat4(self._set_column(key, vector))

    def row(self, key):
        return Vec4(self._row(key))

    def set_row(self, key, vector):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Mat4(self._set_row(key, vector))

    def diagonal(self):
        return Vec4(self._diagonal())

    def set_diagonal(self, vector):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Mat4(self._set_diagonal(vector))

    def inverse(self):
        return Mat4(self._inverse())

    def transform(self, vector):
        assert isinstance(vector, Vec4), "vector must be an instance of Vec4."
        return Vec4(self._transform(vector))

    def hadamard(self, matrix):
        assert isinstance(matrix, Mat4), "matrix must be an instance of Mat4."
        return Mat4(self._hadamard(matrix))

    def divide(self, matrix):
        assert isinstance(matrix, Mat4), "matrix must be an instance of Mat4."
        return Mat4(self._divide(matrix))

    def transpose(self):
        return Mat4(self._transpose())

    def __repr__(self):
        return "<Mat4 \n%s\n>"%self.value

    @classmethod
    def ZERO(cls):
        return Mat4(np.zeros((4,4)))
    @classmethod
    def IDENTITY(cls):
        return Mat4(np.identity(4))
    @classmethod
    def DIAGONAL(cls, value):
        z = np.zeros((4,4))
        np.fill_diagonal(z, value)
        return Mat4(z)
    @classmethod
    def FILLED(cls, value):
        return Mat4(np.full((4,4), value))
    @classmethod
    def VEC4(cls, row1, row2, row3, row4):
        assert isinstance(row1, Vec4) and isinstance(row2, Vec4) and isinstance(row3, Vec4) and isinstance(row4, Vec4)
        return Mat4([row1.elements, row2.elements, row3.elements, row4.elements])
    @classmethod
    def orthographic(cls, left, right, bottom, top, near, far):
        matrix=Mat4.ZERO()
        matrix.value[0][0]=np.divide(2.0,(right-left))
        matrix.value[1][1]=np.divide(2.0,(top-bottom))
        matrix.value[2][2]=np.divide(-2.0,(far-near))
        matrix=matrix.set_column(3, Vec4([-np.divide((right+left),(right-left)), -np.divide((top+bottom),(top-bottom)), -np.divide((far+near),(far-near)),1.0]))
        return matrix

    @classmethod
    def perspective(cls, fov, aspectRatio, near, far):
        matrix=Mat4.FILLED(1.0)
        a=np.tan(np.divide(fov, 2.0))
        b=(far-near)
        matrix.value[0,0]=np.divide(1.0, np.multiply(aspectRatio,a))
        matrix.value[1,1]=np.divide(1.0, a)
        matrix.value[2,2]=-np.divide((far+near),b)
        matrix.value[2,3]=-1.0
        matrix.value[3,2]=-np.divide(np.prod([2.0, far, near]),b)
        return matrix

    @classmethod
    def lookat(cls, camera, object, up):
        assert isinstance(camera,Vec3) and isinstance(object,Vec3) and isinstance(up,Vec3), "Camera, Object, and Up must be instances of Vec3"
        result = Mat4.IDENTITY()
        f = (object-camera).normalize()
        s = f.cross_product(up.normalize())
        u = s.cross_product(f)
        result = result.set_row(Vec4.VEC3(s))
        result = result.set_row(Vec4.VEC3(u))
        result = result.set_row(Vec4.Vec3(f.scalar(-1)))
        return result * Mat4.translate(camera.scalar(-1))


    @classmethod
    def translate(cls, translation):
        assert isinstance(translation, Vec3), "Translation must be instance of Vec3"
        return Mat4.IDENTITY().set_column(3, Vec4([translation[0],translation[1],translation[2],1]))

    @classmethod
    def scale(cls, scale):
        assert isinstance(scale, Vec3), "Scale must be instance of Vec3"
        return Mat4(np.multiply(Mat4.IDENTITY().value, Matrix([[scale[0]],[scale[1]], [scale[2]], [1]]).value))

    @classmethod
    def rotate(cls, angle, axis):
        assert isinstance(axis, Vec3), "Axis must be instance of Vec3"
        result = Mat4.IDENTITY()
        r=radians(angle)
        c=cos(r)
        s=sin(r)
        omc=1.0-c
        x=axis[0]
        y=axis[1]
        z=axis[2]
        result=result.set_column(0, Vec4([np.prod([x,x,omc])+c,np.prod([y,x,omc])+np.prod([z, s]),np.prod([x,z,omc])-np.prod([y, s]), 0]))
        result=result.set_column(1, Vec4([np.prod([x,y,omc])-np.prod([z, s]),np.prod([y,y,omc])+c,np.prod([y,z,omc])+np.prod([x, s]), 0]))
        result=result.set_column(2, Vec4([np.prod([x,z,omc])+np.prod([y, s]),np.prod([y,z,omc])-np.prod([x, s]),np.prod([z,z,omc])+c, 0]))
        return result

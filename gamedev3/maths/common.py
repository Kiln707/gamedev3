import numpy as np
from abc import ABC
from builtins import object

class MathObject(object):
    def invalidTypeException(self, validTypes):
        raise Exception("Invalid type given to %s! Valid types: %s"%(obj.__class__.__name__, validTypes))

    def assert_vector(self, obj):
        if isinstance(obj, Vector):
            return True
        self.invalidTypeException(self, ['Vector'])

    def assert_matrix(self, obj):
        if isinstance(obj, Matrix):
            return True
        self.invalidTypeException(self, ['Matrix'])

    def assert_array(obj):
        if isinstance(obj, np.ndarray):
            return True
        self.invalidTypeException(self, ['Numpy.NDARRAY'])

class Vector(MathObject):
    def __init__(self, values, dimension):
        if isinstance(values, np.ndarray):
            assert len(values) == dimension, "Array of length %s is required for %s"%(dimension, self.__class__.__name__)
            self.value=values
        elif isinstance(values, Vector):
            assert values.dimensions == dimension, "Invalid Vector type! Requires %s but received %s"%(self.__class__.__name__, values.__class__.__name__)
            self.value=values.value
        elif isinstance(values, list):
            assert len(values) == dimension, "List of length %s is required for %s"%(dimension, self.__class__.__name__)
            self.value=np.array(list(values))
        else:
            invalidTypeException(self, ['Vector','list','Numpy.NDARRAY'])

    ########################################
    #   Returns New Vectors. Override These
    ########################################

    def cross_product(self, vector):
        self.assert_vector(vector)
        return Vector(self._cross(vector))

    def hadamard_product(self, vector):
        self.assert_vector(vector)
        assert self._is_same_dimension(vector), "Vectors must be of same dimension"
        return Vector(self._hadamard(vector.value))

    def inverse(self):
        return Vector(self._inverse())

    def transform(self, matrix):
        self.assert_matrix(matrix)
        return Vector(self._transform(matrix.value))

    def normalize(self):
        return Vector(self._normalize())

    def divide(self, vector):
        self.assert_vector(vector)
        self._is_same_dimension(vector)
        return Vector(self._divide(vector.value))

    def add(self, vector):
        self.assert_vector(vector)
        self._is_same_dimension(vector)
        return Vector(self._add(vector.value))

    def subtract(self, vector):
        self.assert_vector(vector)
        self._is_same_dimension(vector)
        return Vector(self._subtract(vector.value))

    def scalar(self, scalar):
        return Vector(self._scalar(scalar))

    def __repr__(self):
        return "<Vector %s>"%self.value

    ######################################
    #   Actual Operations, do not override
    ######################################
    def dot_product(self, vector):
        self.assert_vector(vector)
        self._is_same_dimension(vector)
        return np.dot(self.value.reshape((1, -1)), vector.value)[0]

    def distance(self, vector):
        self.assert_vector(vector)
        self._is_same_dimension(vector)
        return np.sqrt(np.sum(self._hadamard(vector)))

    @property
    def magnitude(self):
        return np.linalg.norm(self.value)

    @property
    def dimensions(self):
        return len(self.value)

    def _is_same_dimension(self, vector):
        return self.dimensions == vector.dimensions

    # Do not override or use below for expected behavior

    def _cross(self, vector):
        self.assert_array(vector)
        if self._is_same_dimension(vector):
            assert len(self.value) == 3, "Cross Product may only be calculated with two 3 dimensional vectors"
        else:
            raise Exception("Vectors are not same size! Cross Product may only be calculated with two 3 dimensional vectors")
        return np.cross(self.value, vector)

    def _hadamard(self, vector):
        self.assert_array(vector)
        return np.multiply(self.value, vector)

    def _scalar(self, scalar):
        return np.multiply(self.value, scalar)

    def _inverse(self):
        return self._scalar(-1)

    def _transform(self, matrix):
        self.assert_array(vector)
        assert self.dimensions == matrix.dimensions[1], "Matrix must have same amount of columns as the dimension of this vector"
        return matrix.dot(self.value)

    def _normalize(self):
        m = self.magnitude
        return np.divide(self.value, m) if m != 0 else 0

    def _divide(self, vector):
        self.assert_array(vector)
        return np.divide(self.value, vector)

    def _add(self, vector):
        return np.add(self.value, vector)

    def _subtract(self, vector):
        self.assert_array(vector)
        return np.subtract(self.value, vector)

    @property
    def elements(self):
        return self.value

    @classmethod
    def DIMENSIONS(cls):
        raise NotImplemented

    ########################################
    #   Builtin Operations, Don't Override
    ########################################
    def __iter__(self):
        for a in self.value:
            yield a

    def __getitem__(self, key):
        return self.value[key]

    def __len__(self):
        return self.magnitude

    def __add__(self, vector):
        return self.add(vector)

    def __sub__(self, vector):
        return self.subtract(vector)

    def __mul__(self, vector):
        return self.dot_product(vector)

    def __truediv__(self, vector):
        return self.divide(vector)

    def __invert__(self):
        return self.inverse()

    def __xor__(self, scalar):
        return self.scalar(scalar)

    def __eq__(self, vector):
        if self.dimensions==vector.dimensions:
            for i in range(0,len(self)):
                if self[i] != vector[i]:
                    return False
            return True
        return False

    def __ne__(self, vector):
        return not self.__eq__(vector)

    def __lt__(self, vector):
        if isinstance(vector, Vector):
            if self.dimensions < vector.dimensions:
                return True
            elif len(vector) == len(self):
                for i in range(0,len(self)):
                    if self[i] < vector[i]:
                        return False
                return True
        return False

    def __le__(self, vector):
        if isinstance(vector, Vector):
            if self.dimensions < vector.dimensions:
                return True
            elif len(vector) == len(self):
                for i in range(0,len(self)):
                    if self[i] <= vector[i]:
                        return False
                return True
        return False

    def __ge__(self, vector):
        if isinstance(vector, Vector):
            if self.dimensions > vector.dimensions:
                return True
            elif len(vector) == len(self):
                for i in range(0,len(self)):
                    if self[i] >= vector[i]:
                        return False
                return True
        return False

    def __gt__(self, vector):
        if isinstance(vector, Vector):
            if self.dimensions > vector.dimensions:
                return True
            elif len(vector) == len(self):
                for i in range(0,len(self)):
                    if self[i] > vector[i]:
                        return False
                return True
        return False

class Matrix(MathObject):

    def __init__(self, values, dimensions):
        if isinstance(values, np.ndarray):
            assert values.shape == dimensions, "Array of length %s is required for %s"%(dimension, self.__class__.__name__)
            self.value=values
        elif isinstance(values, Matrix):
            self.value=values.value
        elif isinstance(values, list):
            assert len(values) == dimensions[0], "list of length %s containing list of length %s is required for %s"%(dimension[0],dimension[1], self.__class__.__name__)
            val=[]
            for v in values:
                if isinstance(v, list):
                    assert len(v) == dimensions[1], "list of length %s containing list of length %s is required for %s"%(dimension[0],dimension[1], self.__class__.__name__)
                    val.append(v)
                elif isinstance(v, Vector):
                    assert v.dimensions == dimensions[1], "list of length %s containing list of length %s is required for %s"%(dimension[0],dimension[1], self.__class__.__name__)
                    val.append(v.value)
                else:
                    self.invalidTypeException(['list(list)', 'list(Vector)'])
            self.value=np.array(val)
        else:
            raise self.invalidTypeException(['Matrix','list','Numpy.NDARRAY'])

    ########################################
    #   Returns New Matricies. Override These
    ########################################

    def add(self, matrix):
        return Matrix(self._add(matrix))

    def subtract(self, matrix):
        return Matrix(self._subtract(matrix))

    def scalar(self, scalar):
        return Matrix(self._scalar(scalar))

    def multiply(self, matrix):
        return Matrix(self._multiply(matrix))

    def column(self, key):
        return Vector(self._column(key))

    def set_column(self, key, value):
        return Matrix(self._set_column(key, value))

    def row(self, key):
        return Vector(self._row(key))

    def set_row(self, key, value):
        return Matrix(self._set_row(key, value))

    def diagonal(self):
        return Vector(self._diagonal())

    def _set_diagonal(self, value):
        return Matrix(self._set_diagonal(value))

    def inverse(self):
        return Matrix(self._inverse())

    def transform(self, vector):
        return Vector(self._transform(vector))

    def hadamard(self, matrix):
        return Matrix(self._hadamard(matrix))

    def divide(self, matrix):
        return Matrix(self._divide(matrix))

    def transpose(self):
        return Matrix(self._transpose())

    def __repr__(self):
        return "<Matrix \n%s\n>"%self.value
    ######################################
    #   Actual Operations, do not override
    ######################################
    @property
    def dimensions(self):
        return self.value.shape

    @property
    def determinant(self):
        return np.linalg.det(self.value)

    @property
    def is_singular(self):
        return self.determinant() == 0

    @property
    def is_square(self):
        return self.value.shape[0] == self.value.shape[1]

    # Do not override or use below for expected behavior
    def _is_same_dimension(self, matrix):
        assert self.dimensions == matrix.dimensions, "Matricies must be the same dimension for this operation"

    def _add(self, matrix):
        self.assert_matrix(matrix)
        self._is_same_dimension(matrix)
        return np.add(self.value, matrix.value)

    def _subtract(self, matrix):
        self.assert_matrix(matrix)
        self._is_same_dimension(matrix)
        return np.subtract(self.value, matrix.value)

    def _scalar(self, scalar):
        return np.multiply(self.value, scalar)

    def _multiply(self, matrix):
        self.assert_matrix(matrix)
        assert self.dimensions[1] == matrix.dimensions[0], "Other Matrix must have same number of Columns as this matrix has Rows"
        return np.matmul(self.value, matrix.value)

    def _column(self, key):
        return self.value.T[key]

    def _set_column(self, key, vector):
        self.assert_vector(vector)
        t=np.copy(self._transpose())
        assert vector.dimensions == len(t[key]), "Invalid length to set column"
        t[key]=vector.value
        return np.copy(t.T)

    def _row(self, key):
        return self.value[key]

    def _set_row(self, key, vector):
        self.assert_vector(vector)
        v = np.copy(self.value)
        assert vector.dimensions == len(v[key]), "Invalid length to set row"
        v[key]=vector.value
        return v

    def _diagonal(self):
        return np.diag(self.value)

    def _set_diagonal(self, vector):
        self.assert_vector(vector)
        v=np.copy(self.value)
        diag=len(np.diag(v))
        assert len(d)==diag, "Invalid Length to set Diagonal"
        for i in range(0, diag):
            v[i][i]=vector[i]
        return v

    def _inverse(self):
        return self.value.getI()

    def _transform(self, vector):
        self.assert_vector(vector)
        assert vector.dimensions == self.dimensions[1], "Matrix must have same amount of columns as the dimension of this vector"
        return self.value.dot(vector.value)

    def _hadamard(self, matrix):
        self.assert_matrix(matrix)
        self._is_same_dimension(matrix)
        return np.multiply(self.value, matrix.value)

    def _divide(self, matrix):
        self.assert_matrix(matrix)
        self._is_same_dimension(matrix)
        return np.divide(self.value, matrix.value)

    def _transpose(self):
        return np.copy(self.value.T)

    @property
    def elements(self):
        return self._transpose()

    ########################################
    #   Builtin Operations, Don't Override
    ########################################
    def __iter__(self):
        for a in self.value:
            yield a

    def __getitem__(self, key):
        return self.value[key]

    def __len__(self):
        return self.dimensions

    def __add__(self, vector):
        return self.add(vector)

    def __sub__(self, vector):
        return self.subtract(vector)

    def __mul__(self, vector):
        return self.multiply(vector)

    def __truediv__(self, vector):
        return self.divide(vector)

    def __invert__(self):
        return self.inverse()

    def __xor__(self, scalar):
        return self.scalar(scalar)

    def __eq__(self, matrix):
        if self.dimensions==matrix.dimensions:
            for i in range(0,len(self)[0]):
                for j in range(0,len(self)[1]):
                    if self.value[i][j] != matrix.value[i][j]:
                        return False
            return True
        return False

    def __ne__(self, vector):
        return not self.__eq__(vector)

    def __lt__(self, matrix):
        if isinstance(matrix, Matrix):
            if self.dimensions < matrix.dimensions:
                return True
            elif len(matrix) == len(self):
                for i in range(0,len(self)[0]):
                    for j in range(0,len(self)[1]):
                        if self.value[i][j] < matrix.value[i][j]:
                            return False
                return True
        return False

    def __le__(self, matrix):
        if isinstance(matrix, Matrix):
            if self.dimensions <= matrix.dimensions:
                return True
            elif len(matrix) == len(self):
                for i in range(0,len(self)[0]):
                    for j in range(0,len(self)[1]):
                        if self.value[i][j] <= matrix.value[i][j]:
                            return False
                return True
        return False

    def __ge__(self, matrix):
        if isinstance(matrix, Matrix):
            if self.dimensions >= matrix.dimensions:
                return True
            elif len(matrix) == len(self):
                for i in range(0,len(self)[0]):
                    for j in range(0,len(self)[1]):
                        if self.value[i][j] >= matrix.value[i][j]:
                            return False
                return True
        return False

    def __gt__(self, matrix):
        if isinstance(matrix, Matrix):
            if self.dimensions > matrix.dimensions:
                return True
            elif len(matrix) == len(self):
                for i in range(0,len(self)[0]):
                    for j in range(0,len(self)[1]):
                        if self.value[i][j] > matrix.value[i][j]:
                            return False
                return True
        return False

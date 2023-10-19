from Geometry import Geometry
from Rectangle import Rectangle
from Circle import Circle
from Cuboid import Cuboid
from Sphere import Sphere

from math import pi

test_shape = Geometry(1,1)
test_rectangle = Rectangle(1,1,1,1)
test_circle = Circle(1,1,1)
test_box = Cuboid(1,1,1,1,1,1)
test_sphere = Sphere(1,1,1,1)

def test_operator_overloads():
    assert test_sphere > test_box
    assert test_circle >= test_rectangle
    assert test_rectangle < test_circle
    assert test_box <= test_sphere

def test_rectangle_geometrics():
    assert test_rectangle.get_area == 1
    assert test_rectangle.get_circumference == 4
    assert test_rectangle.is_square == True
    assert test_rectangle.bot_left == (0.5,0.5)
    assert test_rectangle.top_right == (1.5,1.5)

def test_circle_geometrics():
    assert test_circle.get_area == pi * 1 ** 2
    assert test_circle.get_circumference == 2 * pi * 1
    assert test_circle.is_unit_circle == False

def test_cuboid_geometrics():
    assert test_box.get_volume == 1
    assert test_box.is_cube == True
    assert test_box.bot_left_close == (0.5,0.5,0.5)
    assert test_box.top_right_far == (1.5,1.5,1.5)

def test_sphere_geometrics():
    assert test_sphere.get_volume == (4.0/3.0)*pi*1**3
    assert test_sphere.is_unit_sphere == False

def test_inside_math():
    assert test_rectangle.inside_rectangle_math(1,1) == True
    assert test_circle.inside_circle_math(1,1) == True
    assert test_box.inside_box_math(1,1,1) == True
    assert test_sphere.inside_sphere_math(1,1,1) == True
    assert test_box.is_inside(1,1,1) == True

def test_translate():
    test_circle.translate(1,1)
    assert test_circle.x == 2
    assert test_circle.y == 2
    
    test_sphere.translate(1,1,-1)
    assert test_sphere.x == 2
    assert test_sphere.y == 2
    assert test_sphere.z == 0
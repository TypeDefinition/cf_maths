import unittest
import sys

sys.path.insert(0, 'cf_maths')

import maths_util
import mtx_util
from cf_maths.vec3 import Vec3
from cf_maths.mtx import Mtx
from cf_maths.quat import Quat

class TestQuat(unittest.TestCase):
    def test_conjugate(self):
        a = Quat(4.0, 23.0, 6.0, 7.0)
        b = Quat(4.0, -23.0, -6.0, -7.0)
        self.assertNotEqual(a == b, True)
        self.assertEqual(a.conjugated() == b, True)
        self.assertNotEqual(a.conjugated() != b, True)

    def test_inverse(self):
        a = Quat(4.0, 23.0, 6.0, 8.0)
        b = Quat(4.0 / 645.0, -23.0 / 645.0, -6.0 / 645.0, -8.0 / 645.0)
        self.assertNotEqual(a == b, True)
        self.assertEqual(a.inversed() == b, True)
        self.assertNotEqual(a.inversed() != b, True)

    def test_rotate(self):
        q = Quat.from_axis_angle(Vec3.x_axis(), 45.0 * maths_util.deg2rad)
        m = mtx_util.rotation_matrix_x(45.0 * maths_util.deg2rad)
        self.assertEqual(q.to_rotation_matrix() == m, True)

        q = Quat.from_axis_angle(Vec3.y_axis(), 120.0 * maths_util.deg2rad)
        m = mtx_util.rotation_matrix_y(120.0 * maths_util.deg2rad)
        self.assertEqual(q.to_rotation_matrix() == m, True)

        q = Quat.from_axis_angle(Vec3.z_axis(), 943.0 * maths_util.deg2rad)
        m = mtx_util.rotation_matrix_z(943.0 * maths_util.deg2rad)
        self.assertEqual(q.to_rotation_matrix() == m, True)

        qx = Quat.from_axis_angle(Vec3.x_axis(), 123.0 * maths_util.deg2rad)
        qy = Quat.from_axis_angle(Vec3.y_axis(), 456.0 * maths_util.deg2rad)
        qz = Quat.from_axis_angle(Vec3.z_axis(), 789.0 * maths_util.deg2rad)
        q = qx * qy * qz
        m = mtx_util.rotation_matrix(Vec3(123.0, 456.0, 789.0) * maths_util.deg2rad)
        self.assertEqual(q.to_rotation_matrix() == m, True)

        q = Quat.from_axis_angle(Vec3.x_axis(), 0.0)
        axis_angle = q.to_axis_angle()
        axis = axis_angle[0]
        angle = axis_angle[1]
        self.assertEqual(0.0 == angle, True)
        self.assertEqual(Vec3.x_axis() == axis, True)

        q = Quat.from_axis_angle(Vec3.y_axis(), 0.0)
        axis_angle = q.to_axis_angle()
        axis = axis_angle[0]
        angle = axis_angle[1]
        self.assertEqual(0.0 == angle, True)
        self.assertEqual(Vec3.x_axis() == axis, True)

        q = Quat.from_axis_angle(Vec3.z_axis(), 0.0)
        axis_angle = q.to_axis_angle()
        axis = axis_angle[0]
        angle = axis_angle[1]
        self.assertEqual(0.0 == angle, True)
        self.assertEqual(Vec3.x_axis() == axis, True)

    def test_rotate_point(self):
        a = Vec3(50.0, 0.0, 0.0)
        b = Quat.rotate_via_axis_angle(a, Vec3.y_axis(), maths_util.pi)
        self.assertEqual(b, Vec3(-50.0, 0.0, 0.0))

        a = Vec3(0.0, 10.0, 0.0)
        b = Quat.rotate_via_axis_angle(a, Vec3.y_axis(), maths_util.pi)
        self.assertEqual(b, Vec3(0.0, 10.0, 0.0))

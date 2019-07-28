#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
import unittest
from solid.test.ExpandedTestCase import DiffOutput
from solid import *
from solid.screw_thread import thread, default_thread_section

SEGMENTS = 8


class TestScrewThread(DiffOutput):
    def setUp(self):
        self.tooth_height = 10
        self.tooth_depth = 5
        self.outline = default_thread_section(tooth_height=self.tooth_height, tooth_depth=self.tooth_depth)

    def test_thread(self):
        actual_obj = thread(outline_pts=self.outline, 
                            inner_rad=20, 
                            pitch=self.tooth_height,
                            length=0.75 * self.tooth_height, 
                            segments_per_rot=SEGMENTS,
                            neck_in_degrees=45, 
                            neck_out_degrees=45)
        actual = scad_render(actual_obj)
        expected = '\n\nrender() {\n\tintersection() {\n\t\tpolyhedron(faces = [[0, 1, 3], [1, 4, 3], [1, 2, 4], [2, 5, 4], [0, 5, 2], [0, 3, 5], [3, 4, 6], [4, 7, 6], [4, 5, 7], [5, 8, 7], [3, 8, 5], [3, 6, 8], [6, 7, 9], [7, 10, 9], [7, 8, 10], [8, 11, 10], [6, 11, 8], [6, 9, 11], [9, 10, 12], [10, 13, 12], [10, 11, 13], [11, 14, 13], [9, 14, 11], [9, 12, 14], [12, 13, 15], [13, 16, 15], [13, 14, 16], [14, 17, 16], [12, 17, 14], [12, 15, 17], [15, 16, 18], [16, 19, 18], [16, 17, 19], [17, 20, 19], [15, 20, 17], [15, 18, 20], [0, 2, 1], [18, 19, 20]], points = [[14.9900000000, 0.0000000000, -5.0000000000], [19.9900000000, 0.0000000000, 0.0000000000], [14.9900000000, 0.0000000000, 5.0000000000], [14.1421356237, 14.1421356237, -3.7500000000], [17.6776695297, 17.6776695297, 1.2500000000], [14.1421356237, 14.1421356237, 6.2500000000], [0.0000000000, 20.0000000000, -2.5000000000], [0.0000000000, 25.0000000000, 2.5000000000], [0.0000000000, 20.0000000000, 7.5000000000], [-14.1421356237, 14.1421356237, -1.2500000000], [-17.6776695297, 17.6776695297, 3.7500000000], [-14.1421356237, 14.1421356237, 8.7500000000], [-20.0000000000, 0.0000000000, 0.0000000000], [-25.0000000000, 0.0000000000, 5.0000000000], [-20.0000000000, 0.0000000000, 10.0000000000], [-14.1421356237, -14.1421356237, 1.2500000000], [-17.6776695297, -17.6776695297, 6.2500000000], [-14.1421356237, -14.1421356237, 11.2500000000], [-0.0000000000, -14.9900000000, 2.5000000000], [-0.0000000000, -19.9900000000, 7.5000000000], [-0.0000000000, -14.9900000000, 12.5000000000]]);\n\t\tdifference() {\n\t\t\tcylinder($fn = 8, h = 7.5000000000, r = 25.0100000000);\n\t\t\tcylinder($fn = 8, h = 7.5000000000, r = 20);\n\t\t}\n\t}\n}'
        self.assertEqual(expected, actual)

    def test_thread_internal(self):
        actual_obj = thread(outline_pts=self.outline, 
                            inner_rad=20, 
                            pitch=2 * self.tooth_height,
                            length=2 * self.tooth_height, 
                            segments_per_rot=SEGMENTS,
                            neck_in_degrees=45, 
                            neck_out_degrees=45,
                            external=False)
        actual = scad_render(actual_obj)
        expected = '\n\nrender() {\n\tintersection() {\n\t\tpolyhedron(faces = [[0, 1, 3], [1, 4, 3], [1, 2, 4], [2, 5, 4], [0, 5, 2], [0, 3, 5], [3, 4, 6], [4, 7, 6], [4, 5, 7], [5, 8, 7], [3, 8, 5], [3, 6, 8], [6, 7, 9], [7, 10, 9], [7, 8, 10], [8, 11, 10], [6, 11, 8], [6, 9, 11], [9, 10, 12], [10, 13, 12], [10, 11, 13], [11, 14, 13], [9, 14, 11], [9, 12, 14], [12, 13, 15], [13, 16, 15], [13, 14, 16], [14, 17, 16], [12, 17, 14], [12, 15, 17], [15, 16, 18], [16, 19, 18], [16, 17, 19], [17, 20, 19], [15, 20, 17], [15, 18, 20], [18, 19, 21], [19, 22, 21], [19, 20, 22], [20, 23, 22], [18, 23, 20], [18, 21, 23], [21, 22, 24], [22, 25, 24], [22, 23, 25], [23, 26, 25], [21, 26, 23], [21, 24, 26], [0, 2, 1], [24, 25, 26]], points = [[25.0100000000, 0.0000000000, -5.0000000000], [20.0100000000, 0.0000000000, 0.0000000000], [25.0100000000, 0.0000000000, 5.0000000000], [14.1421356237, 14.1421356237, -2.5000000000], [10.6066017178, 10.6066017178, 2.5000000000], [14.1421356237, 14.1421356237, 7.5000000000], [0.0000000000, 20.0000000000, 0.0000000000], [0.0000000000, 15.0000000000, 5.0000000000], [0.0000000000, 20.0000000000, 10.0000000000], [-14.1421356237, 14.1421356237, 2.5000000000], [-10.6066017178, 10.6066017178, 7.5000000000], [-14.1421356237, 14.1421356237, 12.5000000000], [-20.0000000000, 0.0000000000, 5.0000000000], [-15.0000000000, 0.0000000000, 10.0000000000], [-20.0000000000, 0.0000000000, 15.0000000000], [-14.1421356237, -14.1421356237, 7.5000000000], [-10.6066017178, -10.6066017178, 12.5000000000], [-14.1421356237, -14.1421356237, 17.5000000000], [-0.0000000000, -20.0000000000, 10.0000000000], [-0.0000000000, -15.0000000000, 15.0000000000], [-0.0000000000, -20.0000000000, 20.0000000000], [14.1421356237, -14.1421356237, 12.5000000000], [10.6066017178, -10.6066017178, 17.5000000000], [14.1421356237, -14.1421356237, 22.5000000000], [25.0100000000, -0.0000000000, 15.0000000000], [20.0100000000, -0.0000000000, 20.0000000000], [25.0100000000, -0.0000000000, 25.0000000000]]);\n\t\tcylinder($fn = 8, h = 20, r = 20);\n\t}\n}'
        self.assertEqual(expected, actual)

    def test_default_thread_section(self):
        expected = [[0, -5], [5, 0], [0, 5]]
        actual = default_thread_section(tooth_height=10, tooth_depth=5)
        self.assertEqual(expected, actual)
        
    def test_neck_in_out_degrees(self):
        # Non-specified neck_in_degrees and neck_out_degrees would crash prior
        # to the fix for https://github.com/SolidCode/SolidPython/issues/92
        actual_obj = thread(outline_pts=self.outline, 
                            inner_rad=20, 
                            pitch=self.tooth_height,
                            length=0.75 * self.tooth_height, 
                            segments_per_rot=SEGMENTS,
                            neck_in_degrees=45,
                            neck_out_degrees=0)
        actual = scad_render(actual_obj)        
        expected = '\n\nrender() {\n\tintersection() {\n\t\tpolyhedron(faces = [[0, 1, 3], [1, 4, 3], [1, 2, 4], [2, 5, 4], [0, 5, 2], [0, 3, 5], [3, 4, 6], [4, 7, 6], [4, 5, 7], [5, 8, 7], [3, 8, 5], [3, 6, 8], [6, 7, 9], [7, 10, 9], [7, 8, 10], [8, 11, 10], [6, 11, 8], [6, 9, 11], [9, 10, 12], [10, 13, 12], [10, 11, 13], [11, 14, 13], [9, 14, 11], [9, 12, 14], [12, 13, 15], [13, 16, 15], [13, 14, 16], [14, 17, 16], [12, 17, 14], [12, 15, 17], [15, 16, 18], [16, 19, 18], [16, 17, 19], [17, 20, 19], [15, 20, 17], [15, 18, 20], [0, 2, 1], [18, 19, 20]], points = [[14.9900000000, 0.0000000000, -5.0000000000], [19.9900000000, 0.0000000000, 0.0000000000], [14.9900000000, 0.0000000000, 5.0000000000], [14.1421356237, 14.1421356237, -3.7500000000], [17.6776695297, 17.6776695297, 1.2500000000], [14.1421356237, 14.1421356237, 6.2500000000], [0.0000000000, 20.0000000000, -2.5000000000], [0.0000000000, 25.0000000000, 2.5000000000], [0.0000000000, 20.0000000000, 7.5000000000], [-14.1421356237, 14.1421356237, -1.2500000000], [-17.6776695297, 17.6776695297, 3.7500000000], [-14.1421356237, 14.1421356237, 8.7500000000], [-20.0000000000, 0.0000000000, 0.0000000000], [-25.0000000000, 0.0000000000, 5.0000000000], [-20.0000000000, 0.0000000000, 10.0000000000], [-14.1421356237, -14.1421356237, 1.2500000000], [-17.6776695297, -17.6776695297, 6.2500000000], [-14.1421356237, -14.1421356237, 11.2500000000], [-0.0000000000, -20.0000000000, 2.5000000000], [-0.0000000000, -25.0000000000, 7.5000000000], [-0.0000000000, -20.0000000000, 12.5000000000]]);\n\t\tdifference() {\n\t\t\tcylinder($fn = 8, h = 7.5000000000, r = 25.0100000000);\n\t\t\tcylinder($fn = 8, h = 7.5000000000, r = 20);\n\t\t}\n\t}\n}'
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

import retworkx


class TestHeavyHexGraph(unittest.TestCase):
    def test_heavy_hex_graph_3(self):
        d = 3
        graph = retworkx.generators.heavy_hex_graph(d)
        self.assertEqual(len(graph), (5 * d * d - 2 * d - 1) / 2)
        self.assertEqual(
            len(graph.edges()), 2 * d * (d - 1) + (d + 1) * (d - 1)
        )
        expected_edges = [
            (0, 13),
            (13, 1),
            (1, 14),
            (14, 2),
            (3, 15),
            (15, 4),
            (4, 16),
            (16, 5),
            (6, 17),
            (17, 7),
            (7, 18),
            (18, 8),
            (0, 9),
            (9, 3),
            (5, 12),
            (12, 8),
            (14, 10),
            (10, 16),
            (15, 11),
            (11, 17),
        ]
        self.assertEqual(list(graph.edge_list()), expected_edges)

    def test_heavy_hex_graph_5(self):
        d = 5
        graph = retworkx.generators.heavy_hex_graph(d)
        self.assertEqual(len(graph), (5 * d * d - 2 * d - 1) / 2)
        self.assertEqual(
            len(graph.edges()), 2 * d * (d - 1) + (d + 1) * (d - 1)
        )
        expected_edges = [
            (0, 37),
            (37, 1),
            (1, 38),
            (38, 2),
            (2, 39),
            (39, 3),
            (3, 40),
            (40, 4),
            (5, 41),
            (41, 6),
            (6, 42),
            (42, 7),
            (7, 43),
            (43, 8),
            (8, 44),
            (44, 9),
            (10, 45),
            (45, 11),
            (11, 46),
            (46, 12),
            (12, 47),
            (47, 13),
            (13, 48),
            (48, 14),
            (15, 49),
            (49, 16),
            (16, 50),
            (50, 17),
            (17, 51),
            (51, 18),
            (18, 52),
            (52, 19),
            (20, 53),
            (53, 21),
            (21, 54),
            (54, 22),
            (22, 55),
            (55, 23),
            (23, 56),
            (56, 24),
            (0, 25),
            (25, 5),
            (9, 30),
            (30, 14),
            (10, 31),
            (31, 15),
            (19, 36),
            (36, 24),
            (38, 26),
            (26, 42),
            (40, 27),
            (27, 44),
            (41, 28),
            (28, 45),
            (43, 29),
            (29, 47),
            (46, 32),
            (32, 50),
            (48, 33),
            (33, 52),
            (49, 34),
            (34, 53),
            (51, 35),
            (35, 55),
        ]

        self.assertEqual(list(graph.edge_list()), expected_edges)

    def test_heavy_hex_graph_even_d(self):
        with self.assertRaises(IndexError):
            retworkx.generators.heavy_hex_graph(2)
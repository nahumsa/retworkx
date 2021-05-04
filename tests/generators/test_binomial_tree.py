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


class TestBinomialTreeGraph(unittest.TestCase):

    def test_binomial_tree_graph(self):
        expected_edges = {0: [],
                          1: [(0, 1)],
                          2: [(0, 1), (0, 2), (2, 3)],
                          3: [(0, 1), (0, 2), (0, 4),
                          (2, 3), (4, 5), (4, 6),
                          (6, 7)],
                          4: [(0, 1), (0, 2), (0, 4), (0, 8),
                          (2, 3), (4, 5), (4, 6), (6, 7),
                          (8, 9), (8, 10), (8, 12),
                          (10, 11), (12, 13), (12, 14),
                          (14, 15)]}
        for n in range(5):
            with self.subTest(n=n):
                graph = retworkx.generators.binomial_tree_graph(n)
                self.assertEqual(len(graph), 2**n)
                self.assertEqual(len(graph.edges()), 2**n - 1)
                for edge in list(graph.edge_list()):
                    self.assertIn(edge, expected_edges[n])

    def test_binomial_tree_graph_weights(self):
        graph = retworkx.generators.binomial_tree_graph(
            2, weights=list(range(4)))
        expected_edges = [(0, 1), (0, 2), (0, 4),
                          (2, 3), (4, 5), (4, 6),
                          (6, 7)]
        self.assertEqual(len(graph), 4)
        self.assertEqual([x for x in range(4)], graph.nodes())
        self.assertEqual(len(graph.edges()), 3)
        for edge in list(graph.edge_list()):
            self.assertIn(edge, expected_edges)

    def test_binomial_tree_graph_weight_less_nodes(self):
        graph = retworkx.generators.binomial_tree_graph(
            2, weights=list(range(2)))
        self.assertEqual(len(graph), 4)
        expected_weights = [x for x in range(2)]
        expected_weights.extend([None, None])
        self.assertEqual(expected_weights, graph.nodes())
        self.assertEqual(len(graph.edges()), 3)

    def test_binomial_tree_graph_weights_greater_nodes(self):
        with self.assertRaises(IndexError):
            retworkx.generators.binomial_tree_graph(
                2, weights=list(range(7)))

    def test_binomial_tree_no_order(self):
        with self.assertRaises(TypeError):
            retworkx.generators.binomial_tree_graph(weights=list(range(4)))

    def test_directed_binomial_tree_graph(self):
        expected_edges = {0: [],
                          1: [(0, 1)],
                          2: [(0, 1), (0, 2), (2, 3)],
                          3: [(0, 1), (0, 2), (0, 4),
                          (2, 3), (4, 5), (4, 6),
                          (6, 7)],
                          4: [(0, 1), (0, 2), (0, 4), (0, 8),
                          (2, 3), (4, 5), (4, 6), (6, 7),
                          (8, 9), (8, 10), (8, 12),
                          (10, 11), (12, 13), (12, 14),
                          (14, 15)]}
        for n in range(5):
            with self.subTest(n=n):
                graph = retworkx.generators.directed_binomial_tree_graph(n)
                self.assertEqual(len(graph), 2**n)
                self.assertEqual(len(graph.edges()), 2**n - 1)
                for edge in list(graph.edge_list()):
                    self.assertIn(edge, expected_edges[n])

    def test_directed_binomial_tree_graph_weights(self):
        graph = retworkx.generators.directed_binomial_tree_graph(
            2, weights=list(range(4)))
        self.assertEqual(len(graph), 4)
        self.assertEqual([x for x in range(4)], graph.nodes())
        self.assertEqual(len(graph.edges()), 3)

    def test_directed_binomial_tree_graph_weight_less_nodes(self):
        graph = retworkx.generators.directed_binomial_tree_graph(
            2, weights=list(range(2)))
        self.assertEqual(len(graph), 4)
        expected_weights = [x for x in range(2)]
        expected_weights.extend([None, None])
        self.assertEqual(expected_weights, graph.nodes())
        self.assertEqual(len(graph.edges()), 3)

    def test_directed_binomial_tree_graph_weights_greater_nodes(self):
        with self.assertRaises(IndexError):
            retworkx.generators.directed_binomial_tree_graph(
                2, weights=list(range(7)))

    def test_directed_binomial_tree_no_order(self):
        with self.assertRaises(TypeError):
            retworkx.generators.directed_binomial_tree_graph(
                weights=list(range(4)))
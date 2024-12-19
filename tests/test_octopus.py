import unittest
from octopus import Octopus
from octopus.advanced_operations import AdvancedOperations

class TestOctopus(unittest.TestCase):

    def setUp(self):
        self.octopus = Octopus.Octopus(max_levels=2)

    def test_insert_and_lookup(self):
        self.octopus.insert([0, 1], "Test Data")
        data = self.octopus.lookup([0, 1])
        self.assertEqual(data, "Test Data")

    def test_invalid_insert(self):
        with self.assertRaises(ValueError):
            self.octopus.insert([0, 1, 2], "Test Data")

    def test_delete(self):
        self.octopus.insert([0, 1], "Test Data")
        self.octopus.delete([0, 1])
        data = self.octopus.lookup([0, 1])
        self.assertIsNone(data)

    def test_pathfinding(self):
        self.octopus.insert([0, 1], "Test Data")
        path = self.octopus.pathfinding("d2d2d2d2")
        self.assertEqual(path, [0, 1])

    def test_batch_insert(self):
        adv_ops = AdvancedOperations(self.octopus)
        adv_ops.batch_insert([[0, 1], [0, 2]], ["Data 1", "Data 2"])
        data1 = self.octopus.lookup([0, 1])
        data2 = self.octopus.lookup([0, 2])
        self.assertEqual(data1, "Data 1")
        self.assertEqual(data2, "Data 2")

    def test_subtree_extraction(self):
        self.octopus.insert([0, 1], "Test Data")
        subtree = AdvancedOperations(self.octopus).subtree_extraction([0, 1])
        self.assertEqual(subtree.data, "Test Data")

if __name__ == '__main__':
    unittest.main()
  

import unittest
import LCA
import assignment1
import assignment2
import io
import unittest.mock


class TestCode(unittest.TestCase):
    def test_lca(self):
        test1 = LCA.lca(LCA.child1, LCA.child4)
        test2 = LCA.lca(LCA.child4, LCA.Node(7, None))
        self.assertEqual(test1, 1)
        self.assertEqual(test2, 5)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout1(self, input, expected_output, mock_stdout):
        assignment1.solve(input)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout2(self, input, expected_output, mock_stdout):
        assignment2.solve(input)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_assignment1(self):
        self.assert_stdout1(assignment1.data, "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n")

    def test_assignment2(self):
        self.assert_stdout2(assignment2.data,
                            "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser: 3\nfirst_name: 4\nlast_name: 4\nfather: 4\nfirst_name: 5\nlast_name: 5\nfather: 5\n")

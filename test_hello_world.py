import unittest
from hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    """
    like this yo
    """

    def test_hello_world(self):
        self.assertEquals(HelloWorld().hello('aj'), 'hello there aj')

    # hello there
    def test_hello_not_world(self):
        self.assertNotEquals(HelloWorld().hello('dog'), 'hello there, cat')

    def test_hell0_number(self):
        self.assertEquals(HelloWorld().hello(1), 'hello there, 1')

if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
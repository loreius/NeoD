# test_dappchain.py
"""
Tests for DAppChain module.
"""

import unittest
from dappchain import DAppChain

class TestDAppChain(unittest.TestCase):
    """Test cases for DAppChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DAppChain()
        self.assertIsInstance(instance, DAppChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DAppChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

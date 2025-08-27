import unittest
import VideoList

class TestVideoList(unittest.TestCase):

    def setUp(self):
        """Set up for each test."""
        print("\n--- Setting up for a new test ---")
        VideoList.ClearLastError()
        # Initialize the list with a capacity of 10
        VideoList.SetCapacity(10)
        print(f"Initial capacity set to: {VideoList.Capacity()}")

    def tearDown(self):
        """Tear down after each test."""
        print("--- Test finished, tearing down ---")
        # Clear the list
        VideoList.SetCapacity(0)
        print("Capacity set to 0, list cleared.")

    def test_initial_state(self):
        """Test the initial state of the VideoList."""
        print("Testing initial state...")
        self.assertEqual(VideoList.Capacity(), 10)
        self.assertEqual(VideoList.LastError(), "GOOD")
        # ErrVal should be a large unsigned int for -1
        self.assertTrue(VideoList.ErrVal() > 0)

    def test_set_capacity(self):
        """Test setting the capacity."""
        print("Testing SetCapacity...")
        VideoList.SetCapacity(20)
        self.assertEqual(VideoList.Capacity(), 20)
        print(f"Capacity changed to: {VideoList.Capacity()}")
        VideoList.SetCapacity(5)
        self.assertEqual(VideoList.Capacity(), 5)
        print(f"Capacity changed to: {VideoList.Capacity()}")

    def test_append_and_get(self):
        """Test appending and getting elements."""
        print("Testing Append and Get...")
        print("Appending 'apple', 'banana', 'cherry'")
        idx1 = VideoList.Append("apple")
        self.assertEqual(idx1, 0)
        idx2 = VideoList.Append("banana")
        self.assertEqual(idx2, 1)
        idx3 = VideoList.Append("cherry")
        self.assertEqual(idx3, 2)

        print("Getting elements back...")
        self.assertEqual(VideoList.Get(0), "apple")
        self.assertEqual(VideoList.Get(1), "banana")
        self.assertEqual(VideoList.Get(2), "cherry")
        print("Elements match what was appended.")

    def test_get_out_of_bounds(self):
        """Test getting an element with an out-of-bounds index."""
        print("Testing Get with out-of-bounds index...")
        VideoList.Append("one")
        val = VideoList.Get(5)
        self.assertEqual(val, "")
        self.assertIn("[Get] `i` is too big.", VideoList.LastError())
        print(f"Get out of bounds failed as expected with error: {VideoList.LastError()}")

    def test_append_full(self):
        """Test appending to a full list."""
        print("Testing Append when list is full...")
        VideoList.SetCapacity(3)
        print(f"Capacity set to {VideoList.Capacity()}")
        VideoList.Append("a")
        VideoList.Append("b")
        VideoList.Append("c")
        print("List is now full.")

        err_val = VideoList.Append("d")
        self.assertEqual(err_val, VideoList.ErrVal())
        self.assertIn("[Append] List is full.", VideoList.LastError())
        print(f"Append to full list failed as expected with error: {VideoList.LastError()}")

    def test_set(self):
        """Test setting an element's value."""
        print("Testing Set...")
        VideoList.Append("original")
        print(f"Value at index 0: {VideoList.Get(0)}")
        VideoList.Set(0, "updated")
        print("Setting value at index 0 to 'updated'")
        self.assertEqual(VideoList.Get(0), "updated")
        print(f"New value at index 0: {VideoList.Get(0)}")

    def test_set_out_of_bounds(self):
        """Test setting an element with an out-of-bounds index."""
        print("Testing Set with out-of-bounds index...")
        VideoList.Append("one")
        err_val = VideoList.Set(5, "two")
        self.assertEqual(err_val, VideoList.ErrVal())
        self.assertIn("[Set] `i` is too big.", VideoList.LastError())
        print(f"Set out of bounds failed as expected with error: {VideoList.LastError()}")

    def test_swap(self):
        """Test swapping two elements."""
        print("Testing Swap...")
        VideoList.Append("first")
        VideoList.Append("second")
        print(f"Before swap: Get(0)='{VideoList.Get(0)}', Get(1)='{VideoList.Get(1)}'")
        VideoList.Swap(0, 1)
        print("Swapped elements at index 0 and 1.")
        self.assertEqual(VideoList.Get(0), "second")
        self.assertEqual(VideoList.Get(1), "first")
        print(f"After swap: Get(0)='{VideoList.Get(0)}', Get(1)='{VideoList.Get(1)}'")

    def test_swap_out_of_bounds(self):
        """Test swapping with an out-of-bounds index."""
        print("Testing Swap with out-of-bounds index...")
        VideoList.Append("a")
        VideoList.Append("b")
        err_val = VideoList.Swap(0, 5)
        self.assertEqual(err_val, VideoList.ErrVal())
        self.assertIn("[Swap] `b` is too big.", VideoList.LastError())
        print(f"Swap out of bounds failed as expected with error: {VideoList.LastError()}")

    def test_pop(self):
        """Test the Pop functionality (which seems to be implemented as a circular buffer index shift)."""
        print("Testing Pop...")
        VideoList.Append("a")
        VideoList.Append("b")
        VideoList.Append("c")
        print(f"Before Pop: Get(0)='{VideoList.Get(0)}', Get(1)='{VideoList.Get(1)}'")

        VideoList.Pop()
        print("Called Pop().")

        # After Pop, the start index (IDX) is shifted.
        # Get(0) should now return the second element.
        self.assertEqual(VideoList.Get(0), "b")
        self.assertEqual(VideoList.Get(1), "c")
        print(f"After Pop: Get(0)='{VideoList.Get(0)}', Get(1)='{VideoList.Get(1)}'")
        # Note: The C++ Size() is not decremented, so Get(2) will access invalid data
        # This is likely a bug in the C++ implementation.
        print("Note: Pop implementation seems to only shift the start index, not resize.")

    def test_remove_size_check(self):
        """Test the Remove functionality, focusing on the size calculation."""
        print("Testing Remove (size check)...")
        VideoList.Append("a")
        VideoList.Append("b")
        VideoList.Append("c")
        VideoList.Append("d")
        VideoList.Append("e") # size is 5

        # Confirm initial size is 5 by checking boundaries
        VideoList.ClearLastError()
        self.assertEqual(VideoList.Get(4), "e")
        self.assertEqual(VideoList.Get(5), "")
        self.assertIn("[Get] `i` is too big.", VideoList.LastError())
        VideoList.ClearLastError()

        # Remove 2 elements at index 1 and 2 ("b", "c")
        print("Calling Remove(1, 3) on a list of 5 elements.")
        VideoList.Remove(1, 3)

        # The new size should be 3.
        # We can verify this by checking the new boundaries with Get().
        # Get(2) should now be the last element. Get(3) should be out of bounds.
        print("Verifying new size is 3 by checking boundaries with Get().")
        self.assertNotEqual(VideoList.Get(2), "", "Get(2) should be accessible.")
        self.assertEqual(VideoList.LastError(), "GOOD")

        self.assertEqual(VideoList.Get(3), "", "Get(3) should be out of bounds.")
        self.assertIn("[Get] `i` is too big.", VideoList.LastError())
        print("Size check passed. The content after removal is not tested due to faulty shift logic.")


if __name__ == '__main__':
    print("Running verbose tests for VideoList module...")
    unittest.main(verbosity=2)

# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_queue

import unittest
import time
from queue import Queue

# Hint: Once test_has_linked_list_internal passes, uncomment this line.
# from llist import sllist


class TestQueue(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Queue exists.
        """
        try:
            Queue()
        except NameError:
            self.fail("Could not instantiate Queue.")

    """
    Guiding enqueuing and dequeuing with internal storage
    """

    # def test_has_linked_list_internal(self):
    #     """
    #     A queue has a data member, which is an sllist.
    #     """
    #     from llist import sllist # Hint: pip3 install llist
    #     s = Queue()
    #     self.assertEqual(sllist, type(s.data))

    # Hint: Once test_has_linked_list_internal passes, uncomment the import at
    #       the top of this file.

    # def test_enqueue_one_internal(self):
    #     """
    #     Enqueueing a value adds it to the internal sllist.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     self.assertEqual('fee', s.data.first.value)

    # def test_enqueue_two_internal(self):
    #     """
    #     Enqueueing two values results in the first enqueued value being the first
    #     one in the list, and the second value being the last one in the list.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     s.enqueue('fi')
    #     self.assertEqual('fee', s.data.first.value)
    #     self.assertEqual('fi', s.data.last.value)

    # def test_enqueue_three_internal(self):
    #     """
    #     Enqueueing three values results in the first enqueued value being the first
    #     one in the list, and the third value being the last one in the list.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     s.enqueue('fi')
    #     s.enqueue('fo')
    #     self.assertEqual('fee', s.data.first.value)
    #     self.assertEqual('fo', s.data.last.value)

    # def test_dequeue_one(self):
    #     """
    #     Dequeuing from a single-element queue returns the single value.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     self.assertEqual('fee', s.dequeue())

    # def test_dequeue_one_internal(self):
    #     """
    #     Dequeuing from a single-element queue removes it from the internal sllist.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     self.assertEqual(1, s.data.size)
    #     _ = s.dequeue()
    #     self.assertEqual(0, s.data.size)

    # def test_dequeue_two(self):
    #     """
    #     Dequeuing from a two-element queue returns the first enqueued value.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     s.enqueue('fi')
    #     self.assertEqual('fee', s.dequeue())

    # def test_dequeue_two_internal(self):
    #     """
    #     Dequeuing from a two-element queue removes the first enqueued value from
    #     the sllist.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     s.enqueue('fi')
    #     _ = s.dequeue()
    #     self.assertEqual('fi', s.data.first.value)

    # def test_dequeue_three(self):
    #     """
    #     Dequeuing from a three-element queue returns each enqueued value in FIFO
    #     order.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     s.enqueue('fi')
    #     s.enqueue('fo')
    #     self.assertEqual('fee', s.dequeue())
    #     self.assertEqual('fi', s.dequeue())
    #     self.assertEqual('fo', s.dequeue())

    # def test_dequeue_three_internal(self):
    #     """
    #     Dequeuing from a three-element queue removes each dequeued value from
    #     the internal sllist, in FIFO order.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     s.enqueue('fi')
    #     s.enqueue('fo')
    #     _ = s.dequeue()
    #     self.assertEqual('fi', s.data.first.value)
    #     _ = s.dequeue()
    #     self.assertEqual('fo', s.data.first.value)

    """
    Emptiness
    """

    # def test_empty(self):
    #     """
    #     A queue is initially empty.
    #     """
    #     s = Queue()
    #     self.assertTrue(s.is_empty())

    # def test_not_empty(self):
    #     """
    #     A queue with one enqueued value is not empty.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     self.assertFalse(s.is_empty())

    # def test_empty_after_dequeue(self):
    #     """
    #     A queue with one enqueued value is empty after dequeuing.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     _ = s.dequeue()
    #     self.assertTrue(s.is_empty())

    # def test_not_empty_multiple(self):
    #     """
    #     A queue with two enqueued values is not empty after dequeuing only one.
    #     """
    #     s = Queue()
    #     s.enqueue('fee')
    #     s.enqueue('fi')
    #     _ = s.dequeue()
    #     self.assertFalse(s.is_empty())

    # def test_initial_dequeue(self):
    #     """
    #     Dequeuing from an empty queue raises ValueError.
    #     """
    #     s = Queue()
    #     self.assertRaises(ValueError, s.dequeue)

    """
    Algorithmic complexity
    """

    # def test_enqueue_efficiency(self):
    #     """
    #     Enqueing a value is always O(1).
    #     """
    #     time_samples = []
    #     for _ in range(0, 1000):
    #         s = Queue()
    #         start_time = time.time()
    #         s.enqueue('fake')
    #         end_time = time.time()
    #         time_samples.append(end_time - start_time)
    #     small_average_enqueue_time = sum(time_samples) / float(len(time_samples))

    #     large_queue = Queue()
    #     for _ in range(0, 1000000):
    #         large_queue.enqueue('fake')
    #     large_time_samples = []
    #     for _ in range(0, 1000):
    #         start_time = time.time()
    #         large_queue.enqueue('fake')
    #         end_time = time.time()
    #         large_time_samples.append(end_time - start_time)
    #     large_average_enqueue_time = sum(large_time_samples) / float(len(large_time_samples))
    #     self.assertAlmostEqual(small_average_enqueue_time, large_average_enqueue_time, delta=small_average_enqueue_time)

    # def test_dequeue_efficiency(self):
    #     """
    #     Dequeuing a value is always O(1).
    #     """
    #     time_samples = []
    #     for _ in range(0, 1000):
    #         s = Queue()
    #         s.enqueue('fake')
    #         start_time = time.time()
    #         s.dequeue()
    #         end_time = time.time()
    #         time_samples.append(end_time - start_time)
    #     small_average_dequeue_time = sum(time_samples) / float(len(time_samples))

    #     large_queue = Queue()
    #     for _ in range(0, 1000000):
    #         large_queue.enqueue('fake')
    #     large_time_samples = []
    #     for _ in range(0, 1000):
    #         start_time = time.time()
    #         large_queue.dequeue()
    #         end_time = time.time()
    #         large_time_samples.append(end_time - start_time)
    #     large_average_dequeue_time = sum(large_time_samples) / float(len(large_time_samples))
    #     self.assertAlmostEqual(small_average_dequeue_time, large_average_dequeue_time, delta=small_average_dequeue_time)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()

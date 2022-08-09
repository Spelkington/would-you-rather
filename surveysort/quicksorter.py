import numpy as np
import random

class QuickSorter:

    def __init__(
        self,
        arr: list,
        verbose=False
    ):
        # TODO: Verify all elements of arr are comparible
        self._arr = arr.copy()
        self._max_comparisons = len(self._arr)**2
        self._avg_comparisons = int(len(self._arr) * np.log2(len(self._arr)))
        self._min_comparisons = len(self._arr)
        self._verbose = verbose

    def get_list(self):
        return self._arr

    def sort(self):
        # Begin recording survey stats
        self._num_comparisons_completed = 0
        self._num_items_sorted = 0

        try:
            self._sort(0, len(self._arr) - 1)
            if self._verbose:
                print("Survey Completed.")
        except KeyboardInterrupt:
            if self._verbose:
                print("Survey terminated.")

        if self._verbose:
            print(f"Questions Answered: {self._num_comparisons_completed} out of:")
            print(f"\t{self._min_comparisons} minimum")
            print(f"\t{self._avg_comparisons} average")
            print(f"\t{self._max_comparisons} maximum")

            # TODO: Fix number sorted tracker
            # print()
            # print(f"The first {self._num_items_sorted} elements were sorted correctly.")

        return self.get_list()

    def _sort(self, lower, upper):
        if lower < upper:
            partition_boundary = self._partition(lower, upper)

            # NOTE: Sorting the right partition before the left is a conscious decision that
            #       should not be swapped. Because this is a survey capable of early
            #       user termination, sorting the right-hand side first means that large
            #       values will be sorted before small values. In the context of
            #       Situations, it means that the survey will complete in the order of
            #       most-favorite to least-favorite.
            self._sort(partition_boundary + 1, upper)
            self._sort(lower, partition_boundary - 1)
        else:
            # TODO: fix number sorted tracker
            self._num_items_sorted += 0


    def _partition(self, lower, upper):
        i_pivot = upper
        pivot = self._arr[i_pivot]
        self._swap(i_pivot, upper)

        i_current = lower - 1
        i_scanner = lower
        while i_scanner < upper:
            
            if self._verbose:
                print(f"Questions {self._num_comparisons_completed} out of:")
                print(f"\t{self._min_comparisons} minimum")
                print(f"\t{self._avg_comparisons} average")
                print(f"\t{self._max_comparisons} maximum")

            # If item at scanner index was less than the item at the current
            # index, increment the current index and swap
            if self._arr[i_scanner] < pivot:
                i_current += 1
                self._swap(i_current, i_scanner)
            
            # Increment number of comparisons completed
            self._num_comparisons_completed += 1

            # Increment the scanner index to analyze the following element
            i_scanner += 1

        # Place the pivot back into the current position after the current index
        self._swap(i_current + 1, upper)
        
        # Return the position of the pivot index
        return i_current + 1


    def _swap(self, i_first, i_second):
        temp = self._arr[i_first]
        self._arr[i_first] = self._arr[i_second]
        self._arr[i_second] = temp
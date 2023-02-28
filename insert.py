def insert_into_array(self, arr, index, arr_to_insert):
        """
        Insert a given array  of characters (typically the same characters but split on a different delimeter) into an index
        Example:
          I want to insert ['y', '=', '2'] into below at the 11th index,
            ['select', 'one', 'two', 'three', 'from', 'foo', 'where', 'x', '=', '1', 'and', ** 'orderby', 'x;']
            (In this example the given index was a statement that was previously y=2, but the program assumes that it has been removed)
            --> 
            ['select', 'one', 'two', 'three', 'from', 'foo', 'where', 'x', '=', '1', 'and', *'y', '=', '2'*, 'orderby', 'x;']

        NOTE: This can easily be updated to simply insert without removing the element from the list by removing the index+1 on the right var

        Args:
            arr (array): original array containing element to replace
            index (int): index of element to be replaced
            arr_to_insert (array): the array to be inserted

        Returns:
            array : updated array after replacement.
        """
        if index >= len(arr):
            print("Index to replace larger than allowed")
            return []
        left = arr[:index]
        right = arr[index:]
        return [*left, *arr_to_insert, *right]

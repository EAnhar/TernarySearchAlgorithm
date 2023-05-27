# Ternary Search Algorithm
 it is a divide-and-conquer algorithm that is used to find the position of a specific value in a given sorted array or list.
 
## How it's Work ?
 
Step 1: Divide  the list in three parts with two mid-points

Step 2: Check if key is present at any mid  go to step 3, if not repeat the search operation and predict in which section the target element lies. The search space is reduced to 1/3rd. If the element is not in the list, go to step 4 or to step 1.

Step 3: Element found. Return index and exit.

Step 4: Element not found. Exit.

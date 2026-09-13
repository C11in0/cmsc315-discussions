# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## Reflection

In this assignment, I learned how linear search and binary search use different approaches to find values in a dataset. I implemented linear search by checking each value in order until the target was found. I also implemented binary search, which repeatedly divided the search area in half. Testing both algorithms helped me better understand why linear search has O(n) time complexity while binary search has O(log n) time complexity.

One challenge I encountered was understanding how binary search changed the left and right boundaries after checking the middle value. I overcame this by following how the search area became smaller after each comparison. Testing an empty list, a single-element list, and values at the beginning and end of the list also helped me understand how the algorithms handled different situations.

I learned that binary search was more efficient for large, sorted datasets. However, linear search was useful when data was unsorted or when searching a small collection where sorting the data first would add unnecessary work. Binary search would not be usable directly on an unsorted list because it depends on the values being arranged in order.
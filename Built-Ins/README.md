# Python Custom Sorting Guide 🐍

This guide provides practical examples of sorting dictionaries and $N \times M$ matrices using `itemgetter`, `lambda`, and multi-column logic.

---

## 1. Sorting Dictionaries
When sorting a list of dictionaries, the `key` identifies which dictionary value to compare.

### Using `lambda`
Best for quick, one-off sorting without imports.
```python
data = [
    {'name': 'Alice', 'age': 30}, 
    {'name': 'Bob', 'age': 25}
]
# Sort by age
sorted_data = sorted(data, key=lambda x: x['age'])
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
```
### Using `itemgetter`
More efficient for large datasets as it runs at C-speed.
```python
from operator import itemgetter

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

# Sort by name
sorted_data = sorted(data, key=itemgetter('name'))
```
### `Multi-Column Sorting (Tie-Breaking)`
Sort by one key, then another as a secondary priority.
```python
data = [
    {'name': 'Alice', 'score': 90},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 85}
]

# Sort by score (descending), then name (ascending)
sorted_data = sorted(data, key=lambda x: (-x['score'], x['name']))
```
---
## 2. Sorting $N \times M$ Matrices
When sorting a list of lists (2D Array), the `key` refers to the column index.

### Using `lambda`
```python
matrix = [
    [10, 30], 
    [20, 10], 
    [15, 20]
]

# Sort by the second column (index 1)
sorted_matrix = sorted(matrix, key=lambda row: row[1])
# Output: [[20, 10], [15, 20], [10, 30]]
```
### Using `itemgetter`
The most readable way to target specific column indices.
```python
from operator import itemgetter

matrix = [[10, 30], [20, 10], [15, 20]]

# Sort by the first column (index 0)
sorted_matrix = sorted(matrix, key=itemgetter(0))
```
### `Multi-Column Sorting`
Useful when you need to order rows based on multiple column priorities.
```python
matrix = [
    [1, 5, 10],
    [2, 2, 20],
    [1, 2, 30]
]

# Primary sort: Column 0, Secondary sort: Column 1
sorted_matrix = sorted(matrix, key=itemgetter(0, 1))
# Output: [[1, 2, 30], [1, 5, 10], [2, 2, 20]]
```
## Summary Table
| Method | Best Use Case | Performance |
| :--- | :--- | :--- |
| **Lambda** | Simple logic, no imports | Standard |
| **Itemgetter** | Fixed indices/keys, large data | **High** |
| **Tuple Key** | Complex tie-breaking | Standard |

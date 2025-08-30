**table mapping common operations to list, set, and dict** in Python, along with their **average-case time complexity**:

| Operation                     | List                   | Set                           | Dict                           |
| ----------------------------- | ---------------------- | ----------------------------- | ------------------------------ |
| **Access / Lookup**           | `lst[i]` → O(1)        | Not directly (use membership) | `d[key]` → O(1)                |
| **Insertion**                 | `lst.append(x)` → O(1) | `s.add(x)` → O(1)             | `d[key] = val` → O(1)          |
| **Deletion**                  | `lst.pop(i)` → O(n)    | `s.remove(x)` → O(1)          | `del d[key]` → O(1)            |
| **Search / Membership check** | `x in lst` → O(n)      | `x in s` → O(1)               | `key in d` → O(1)              |
| **Traversal / Iteration**     | `for x in lst:` → O(n) | `for x in s:` → O(n)          | `for k, v in d.items()` → O(n) |
| **Update / Modify**           | `lst[i] = x` → O(1)    | Not applicable                | `d[key] = new_val` → O(1)      |

---

**Key takeaways:**

* **Lists** are slower for membership/search because they check sequentially → O(n).
* **Sets & Dicts** use hash tables → most operations are O(1) average-case.
* Traversal is O(n) for all because you have to visit each element.

---

### **1️. List**

```
Memory (contiguous array of references):

Index:   0     1     2     3     4
List:   [10]  [20]  [30]  [40]  [50]

Operations:
- Access: lst[2] → 30 (direct index)
- Insertion: lst.append(60) → add at next free slot
- Deletion: lst.pop(1) → remove 20, shift remaining elements
- Search: 50 in lst → check sequentially
- Traversal: for x in lst: ...
```

---

### **2️. Set**

```
Memory (hash table with buckets):

Bucket 0 -> [40]
Bucket 1 -> [10]
Bucket 2 -> [30, 50]  <- collision
Bucket 3 -> [20]

Operations:
- Insertion: s.add(60) → hash(60) % num_buckets → bucket
- Membership: 50 in s → hash(50) → go to bucket → check elements in bucket
- Deletion: s.remove(30) → hash(30) → bucket → remove
- Traversal: for x in s → iterate buckets
```

* Elements in bucket may not be sorted.
* Lookup is fast O(1) on average.

---

### **3️. Dict**

```
Memory (hash table with buckets storing key-value pairs):

Bucket 0 -> [("d", 40)]
Bucket 1 -> [("a", 10)]
Bucket 2 -> [("c", 30), ("e", 50)]  <- collision
Bucket 3 -> [("b", 20)]

Operations:
- Access: d["c"] → hash("c") → bucket → find key → 30
- Insertion: d["f"] = 60 → hash("f") → bucket → add
- Deletion: del d["e"] → hash("e") → bucket → remove key-value
- Membership: "b" in d → hash("b") → bucket → check key
- Traversal: for k, v in d.items() → iterate all buckets
```

---

**Key visualization takeaways:**

* **List** → contiguous, sequential access, slower search
* **Set** → hash table, fast lookup, unordered, collisions handled inside buckets
* **Dict** → hash table with key-value pairs, fast key lookup, collisions handled

---

### Quick Tip

- **1 call** per function → linear recursion → **O(n)**
- **Multiple calls** per function → tree/exponential recursion → **O(2^n) or O(k^n)**
- **Divide input** each call → divide & conquer → **O(log n)**
# HW/LAB#7: More NumPy

### Tasks:

1. **Boolean Arrays & Masks (Section 2.06)**

   - **Basic Rainy Day Count:**  
     Use a Boolean mask to find how many days had rain (i.e., rainfall > 0 mm).

   - **Heavy Rain Days:**  
     Find the percentage of days where rainfall exceeded 5 mm.

   - **Dry Spells:**  
     Find the longest consecutive sequence of dry days (rainfall == 0).

---

2. **Fancy Indexing (Section 2.07)**

   - **Top Rainfall Days:**  
     Find the 10 wettest days of the year using fancy indexing.

   - **Monthly Averages:**  
     Assume the data starts on January 1st. Compute the average monthly rainfall using fancy indexing.

---

3. **Sorting (Section 2.08)**

   - **Sorting Rainfall Data:**  
     Sort the rainfall array in ascending order and find the median rainfall value.

   - **Percentile Analysis:**  
     Find the 90th percentile of rainfall (i.e., the rainfall value above which only 10% of days occur).

---

4. **Structured Data (Section 2.09)**

   - **Creating a Structured Array:**  
     Create a structured NumPy array where each entry contains:

     - `day` (integer, 1 to 365)
     - `rainfall` (float, in mm)
     - `is_rainy` (Boolean, `True` if rainfall > 0)

   - **Filtering Data with Structured Arrays:**  
     Use Boolean masks on the structured array to extract all rainy days and compute their average rainfall.

   - **Sorting Structured Data:**  
     Sort the structured array by rainfall and print the top 5 rainiest days.

---

## Dataset:

You are provided with an array representing daily rainfall (in mm) over a year in a fictional city:

```python
import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)  # Synthetic daily rainfall data

rainfall[np.random.choice(365, 100, replace=False)] = 0  # 100 dry days
```

---

### 1. **Boolean Arrays & Masks (Section 2.06)**

#### **Basic Rainy Day Count:**

- Use a Boolean mask to find how many days had rain (i.e., where `rainfall > 0 mm`).

#### **Heavy Rain Days:**

- Find the percentage of days where rainfall exceeded 5 mm.

#### **Dry Spells:**

- Find the longest consecutive sequence of dry days (rainfall == 0).

---

### 2. **Fancy Indexing (Section 2.07)**

#### **Top Rainfall Days:**

- Find the 10 wettest days of the year using fancy indexing.

#### **Monthly Averages:**

- Assume the data starts on January 1st. Compute the average monthly rainfall using fancy indexing.

---

### 3. **Sorting (Section 2.08)**

#### **Sorting Rainfall Data:**

- Sort the rainfall array in ascending order and find the median rainfall value.

#### **Percentile Analysis:**

- Find the 90th percentile of rainfall (i.e., the rainfall value above which only 10% of days occur).

---

### 4. **Structured Data (Section 2.09)**

#### **Creating a Structured Array:**

- Create a structured NumPy array where each entry contains:
  - `day` (integer, 1 to 365)
  - `rainfall` (float, in mm)
  - `is_rainy` (Boolean, `True` if rainfall > 0)

#### **Filtering Data with Structured Arrays:**

- Use Boolean masks on the structured array to extract all rainy days and compute their average rainfall.

#### **Sorting Structured Data:**

- Sort the structured array by rainfall and print the top 5 rainiest days.

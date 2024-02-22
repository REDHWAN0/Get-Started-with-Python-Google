<h1>Activity: Dataframes with pandas</h1>

## Introduction

Your work as a data professional for the U.S. Environmental Protection Agency (EPA) requires you to analyze air quality index data collected from the United States and Mexico.

The air quality index (AQI) is a number that runs from 0 to 500. The higher the AQI value, the greater the level of air pollution and the greater the health concern. For example, an AQI value of 50 or below represents good air quality, while an AQI value over 300 represents hazardous air quality. Refer to this guide from [AirNow.gov](https://www.airnow.gov/aqi/aqi-basics/) for more information.

In this lab, you will practice working in pandas. You will load a dataframe, examine its metadata and summary statistics, and explore it using iloc indexing and sorting. You will also practice Boolean masking, grouping, and concatenating data.

## Tips for completing this lab

As you navigate this lab, keep the following tips in mind:

- `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
- Feel free to open the hints for additional guidance as you work on each task.
- To enter your answer to a question, double-click the markdown cell to edit. Be sure to replace the "[Double-click to enter your responses here.]" with your own answer.
- You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook.
- You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook.

## Task 1: Read data from csv file into a pandas dataframe

You are given two files of data. Begin with the first file, which contains the three states with the most observations (rows): California, Texas, and Pennsylvania.

### 1a: Import statements

Import numpy and pandas. Use their standard aliases.


```python
### YOUR CODE HERE ###
import numpy as np
import pandas as pd

```

<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

Begin with the `import` keyword for each statement.

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

Use the `as` keyword to assign an alias.

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

The conventional aliases are `np` for numpy and `pd` for pandas.

</details>

### 1b: Read in the first file

1. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

2. Use the `head()` method on the `top3` dataframe to inspect the first five rows.


```python
# 1. ### YOUR CODE HERE ###
top3 = pd.read_csv('epa_ca_tx_pa.csv')

# 2. ### YOUR CODE HERE ###
top3.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state_code</th>
      <th>state_name</th>
      <th>county_code</th>
      <th>county_name</th>
      <th>aqi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6</td>
      <td>California</td>
      <td>1</td>
      <td>Alameda</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>California</td>
      <td>7</td>
      <td>Butte</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>California</td>
      <td>19</td>
      <td>Fresno</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>California</td>
      <td>29</td>
      <td>Kern</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>California</td>
      <td>29</td>
      <td>Kern</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



<details>
  <summary><h4><strong>Hint</strong></h4></summary>

Because the file is already in your working directory, you can simply pass the file name to the `pd.read_csv()` function as a string.

</details>

## Task 2: Summary information

Now that you have a dataframe with the AQI data for California, Texas, and Pennsylvania, get some high-level summary information about it.

### 2a: Metadata

Use a DataFrame method to examine the number of rows and columns, the column names, the data type contained in each column, the number of non-null values in each column, and the amount of memory the dataframe uses.


```python
### YOUR CODE HERE ###
top3.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 546 entries, 0 to 545
    Data columns (total 5 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   state_code   546 non-null    int64  
     1   state_name   546 non-null    object 
     2   county_code  546 non-null    int64  
     3   county_name  546 non-null    object 
     4   aqi          546 non-null    float64
    dtypes: float64(1), int64(2), object(2)
    memory usage: 21.5+ KB


<details>
  <summary><h4><strong>Hint</strong></h4></summary>

The `info()` method returns a dataframe's metadata.

</details>

### 2b: Summary statistics

Examine the summary statistics of the dataframe's numeric columns. The output should be a table that includes row count, mean, standard deviation, min, max, and quartile values.


```python
### YOUR CODE HERE ###
top3.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state_code</th>
      <th>county_code</th>
      <th>aqi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>546.000000</td>
      <td>546.000000</td>
      <td>546.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>20.593407</td>
      <td>83.179487</td>
      <td>8.906593</td>
    </tr>
    <tr>
      <th>std</th>
      <td>19.001484</td>
      <td>92.240873</td>
      <td>9.078479</td>
    </tr>
    <tr>
      <th>min</th>
      <td>6.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>6.000000</td>
      <td>29.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.000000</td>
      <td>66.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>42.000000</td>
      <td>98.500000</td>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>48.000000</td>
      <td>479.000000</td>
      <td>93.000000</td>
    </tr>
  </tbody>
</table>
</div>



<details>
  <summary><h4><strong>Hint</strong></h4></summary>

The `describe()` method returns a table of summary statistics for a dataframe's numeric columns.

</details>

## Task 3: Explore your data

Practice exploring your data by completing the following exercises.

### 3a: Rows per state

Select the `state_name` column and use the `value_counts()` method on it to check how many rows there are for each state in the dataframe.


```python
### YOUR CODE HERE ###
top3['state_name'].value_counts()
```




    California      342
    Texas           104
    Pennsylvania    100
    Name: state_name, dtype: int64



<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

This code should all be on a single line. Begin by selecting the `top3` dataframe at the `state_name` column. You can use either selector brackets or dot notation.

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

When using brackets to select a column, the column's name should be entered as a string.

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

The `value_counts()` method is added to the end of the selection statement using dot notation. Its parentheses are empty.

</details>

### 3b: Sort by AQI

1.  Create a new dataframe called `top3_sorted` by using the `sort_values()` method on the `top3` dataframe. Refer to the [sort_values pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#) for more information about how to use this method.
    *  The new dataframe should contain the data sorted by AQI, beginning with the rows with the highest AQI values.
2.  Print the top 10 rows of `top3_sorted`.


```python
# 1. ### YOUR CODE HERE ###
top3_sorted = top3.sort_values(by = 'aqi', ascending = False)

# 2. ### YOUR CODE HERE ###
top3_sorted.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state_code</th>
      <th>state_name</th>
      <th>county_code</th>
      <th>county_name</th>
      <th>aqi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>76</th>
      <td>6</td>
      <td>California</td>
      <td>37</td>
      <td>Los Angeles</td>
      <td>93.0</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6</td>
      <td>California</td>
      <td>37</td>
      <td>Los Angeles</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>6</td>
      <td>California</td>
      <td>83</td>
      <td>Santa Barbara</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>122</th>
      <td>6</td>
      <td>California</td>
      <td>59</td>
      <td>Orange</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>184</th>
      <td>6</td>
      <td>California</td>
      <td>59</td>
      <td>Orange</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>51</th>
      <td>48</td>
      <td>Texas</td>
      <td>141</td>
      <td>El Paso</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>80</th>
      <td>6</td>
      <td>California</td>
      <td>65</td>
      <td>Riverside</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>136</th>
      <td>48</td>
      <td>Texas</td>
      <td>141</td>
      <td>El Paso</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>6</td>
      <td>California</td>
      <td>65</td>
      <td>Riverside</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>48</td>
      <td>Texas</td>
      <td>141</td>
      <td>El Paso</td>
      <td>40.0</td>
    </tr>
  </tbody>
</table>
</div>



<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

Attach the `sort_values()` method to the `top3` dataframe using dot notation.

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

*  The `by` argument of the `sort_values()` method should be a string of the column you want to sort by.

*  The default behavior of the `sort_values()` method is to sort in ascending order. You want to sort in *descending* order. Which keyword argument modifies this behavior? Refer to the [sort_values() pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#).

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

*  Use the `head()` method on the `top3_sorted` dataframe.

*  The default behavior of the `head()` method is to print the first five rows of a dataframe. You want to print the first 10 rows. Refer to the [head() pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) for more information on how to modify this behavior.


</details>

### 3c: Use `iloc` to select rows

Use `iloc` to select the two rows at indices 10 and 11 of the `top3_sorted` dataframe.


```python
### YOUR CODE HERE ###
top3_sorted.iloc[10:12]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state_code</th>
      <th>state_name</th>
      <th>county_code</th>
      <th>county_name</th>
      <th>aqi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>186</th>
      <td>6</td>
      <td>California</td>
      <td>73</td>
      <td>San Diego</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>74</th>
      <td>6</td>
      <td>California</td>
      <td>37</td>
      <td>Los Angeles</td>
      <td>38.0</td>
    </tr>
  </tbody>
</table>
</div>



<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

To use `iloc` on the `top3_sorted` dataframe, use dot notation.

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

`iloc` uses brackets to index data.

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

`iloc` index ranges are separated by a colon. Remember, the end index is not included in the range of returned indices.

</details>

## Task 4: Examine California data

You notice that the rows with the highest AQI represent data from California, so you want to examine the data for just the state of California.

### 4a: Basic Boolean masking

1. Create a Boolean mask that selects only the observations of the `top3_sorted` dataframe that are from California.
2. Apply the Boolean mask to the `top3_sorted` dataframe and assign the result to a variable called `ca_df`.
3. Print the first five rows of `ca_df`.


```python
# 1. ### YOUR CODE HERE ###
mask = top3_sorted['state_name'] == 'California'

# 2. ### YOUR CODE HERE ###
ca_df = top3_sorted[mask]


# 3. ### YOUR CODE HERE ###
ca_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state_code</th>
      <th>state_name</th>
      <th>county_code</th>
      <th>county_name</th>
      <th>aqi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>76</th>
      <td>6</td>
      <td>California</td>
      <td>37</td>
      <td>Los Angeles</td>
      <td>93.0</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6</td>
      <td>California</td>
      <td>37</td>
      <td>Los Angeles</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>6</td>
      <td>California</td>
      <td>83</td>
      <td>Santa Barbara</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>122</th>
      <td>6</td>
      <td>California</td>
      <td>59</td>
      <td>Orange</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>184</th>
      <td>6</td>
      <td>California</td>
      <td>59</td>
      <td>Orange</td>
      <td>47.0</td>
    </tr>
  </tbody>
</table>
</div>



<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

Refer to what you've learned about Boolean masking.

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

Define a `mask` variable that is the `top3_sorted` dataframe selected where the `state_name` column is `California`.

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

*  Apply the `mask` variable to the `top3_sorted` dataframe and assign the result to a new dataframe called `ca_df`.

*  Use the `head()` method on the new `ca_df` dataframe.
</details>

### 4b: Validate CA data

Inspect the shape of your new `ca_df` dataframe. Does its row count match the number of California rows determined in Task 3a?


```python
### YOUR CODE HERE ###
ca_df.shape
```




    (342, 5)



<details>
  <summary><h4><strong>Hint</strong></h4></summary>

*   Use the `shape` attribute on the `ca_df` dataframe.

*   Attributes don't use parentheses.


</details>

### 4c: Rows per CA county

Examine a list of the number of times each county is represented in the California data.


```python
### YOUR CODE HERE ###
ca_df['county_name'].value_counts()
```




    Los Angeles        55
    Santa Barbara      26
    San Bernardino     21
    Orange             19
    San Diego          19
    Sacramento         17
    Alameda            17
    Fresno             16
    Riverside          14
    Contra Costa       13
    Imperial           13
    San Francisco       8
    Monterey            8
    Humboldt            8
    Santa Clara         7
    El Dorado           7
    Placer              6
    Butte               6
    Kern                6
    Mendocino           6
    Solano              5
    San Joaquin         5
    Tulare              5
    Ventura             5
    Sutter              4
    San Mateo           4
    Marin               3
    Sonoma              3
    Stanislaus          3
    San Luis Obispo     2
    Napa                2
    Santa Cruz          2
    Calaveras           2
    Shasta              1
    Tuolumne            1
    Inyo                1
    Yolo                1
    Mono                1
    Name: county_name, dtype: int64



<details>
  <summary><h4><strong>Hint</strong></h4></summary>

Select the `county_name` column of `ca_df` and apply the `value_counts()` method to it using dot notation.

</details>

### 4d: Calculate mean AQI for Los Angeles county

You notice that Los Angeles county has more than twice the number of rows of the next-most-represented county in California, and you want to learn more about it.

*  Calculate the mean AQI for LA county.


```python
### YOUR CODE HERE ###
mask = ca_df['county_name'] == 'Los Angeles'
ca_df[mask]['aqi'].mean()
```




    9.412280701754385



<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

Use Boolean masking to create a mask. Then apply the mask to the `ca_df` dataframe, select the `aqi` column of the result, and calculate its mean.

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

The Boolean mask is `ca_df` selected where `county_name` is `Los Angeles`.

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

*  Apply the Boolean mask to `ca_df`.
*  Then use selector brackets to select the `aqi` column.
*  Then use dot notation to attach the `mean()` method to the end of the expression.

</details>

## Task 5: Groupby

Group the original dataframe (`top3`) by state and calculate the mean AQI for each state.


```python
### YOUR CODE HERE ###
top3.groupby('state_name').mean()[['aqi']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>aqi</th>
    </tr>
    <tr>
      <th>state_name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>California</th>
      <td>9.412281</td>
    </tr>
    <tr>
      <th>Pennsylvania</th>
      <td>6.690000</td>
    </tr>
    <tr>
      <th>Texas</th>
      <td>9.375000</td>
    </tr>
  </tbody>
</table>
</div>



<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

Use the `groupby()` method on the `top3` dataframe.

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

Group by `state_name` and use dot notation to chain the `mean()` method to the expression.

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

`top3.groupby('state_name').mean()` will produce a table of the mean values of every numeric column for each state. To filter the table on just the `aqi` column, add `['aqi']` to the end of the expression.

</details>

## Task 6: Add more data

Now that you have performed a short examination of the file with AQI data for California, Texas, and Pennsylvania, you want to add more data from your second file.

### 6a: Read in the second file

1. Read in the data for the remaining territories. The file is called `'epa_others.csv'` and is already in your working directory. Assign the resulting dataframe to a variable named `other_states`.

2. Use the `head()` method on the `other_states` dataframe to inspect the first five rows.


```python
# 1. ### YOUR CODE HERE ###
other_states = pd.read_csv('epa_others.csv')

# 2. ### YOUR CODE HERE ###
other_states.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state_code</th>
      <th>state_name</th>
      <th>county_code</th>
      <th>county_name</th>
      <th>aqi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Arizona</td>
      <td>13</td>
      <td>Maricopa</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Arizona</td>
      <td>13</td>
      <td>Maricopa</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Arizona</td>
      <td>19</td>
      <td>Pima</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>Colorado</td>
      <td>41</td>
      <td>El Paso</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12</td>
      <td>Florida</td>
      <td>31</td>
      <td>Duval</td>
      <td>15.0</td>
    </tr>
  </tbody>
</table>
</div>



### 6b: Concatenate the data

The data from `other_states` is in the same format as the data from `top3`. It has the same columns in the same order.

1. Add the data from `other_states` as new rows beneath the data from `top3`. Assign the result to a new dataframe called `combined_df`.

2. Verify that the length of `combined_df` is equal to the sum of the lengths of `top3` and `other_states`.


```python
# 1. ### YOUR CODE HERE ###
combined_df = pd.concat([top3, other_states], axis = 0)

# 2. ### YOUR CODE HERE ###
len(combined_df) == len(top3) + len(other_states)
```




    True



<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

Use the `concat()` function. For more information on this function, refer to the [concat() pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.concat.html).

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

*  Enter the two dataframes being joined as a list in the argument field of the `concat()` function.

*  To add rows, concatenate along axis 0. To add columns, concatenate along axis 1.

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

Use the `len()` function in a comparison statement to determine if the length of `combined_df` equals the length of `top3` plus the length of `other_states`.

</details>

## Task 7: Complex Boolean masking

According to the EPA, AQI values of 51-100 are considered of "Moderate" concern. You've been tasked with examining some data for the state of Washington.

*  Use Boolean masking to return the rows that represent data from the state of Washington with AQI values of 51+.


```python
### YOUR CODE HERE ###
mask = (combined_df['state_name'] == 'Washington') & (combined_df['aqi'] >= 51)
combined_df[mask]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state_code</th>
      <th>state_name</th>
      <th>county_code</th>
      <th>county_name</th>
      <th>aqi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40</th>
      <td>53</td>
      <td>Washington</td>
      <td>33</td>
      <td>King</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>53</td>
      <td>Washington</td>
      <td>61</td>
      <td>Snohomish</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>121</th>
      <td>53</td>
      <td>Washington</td>
      <td>77</td>
      <td>Yakima</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>122</th>
      <td>53</td>
      <td>Washington</td>
      <td>77</td>
      <td>Yakima</td>
      <td>57.0</td>
    </tr>
  </tbody>
</table>
</div>



<details>
  <summary><h4><strong>Hint 1</strong></h4></summary>

Create a Boolean mask for `combined_df` with two conditions:

*   The state is Washington
*   The AQI is greater than or equal to 51

</details>

<details>
  <summary><h4><strong>Hint 2</strong></h4></summary>

Remember to enclose each condition in its own set of parentheses.

</details>

<details>
  <summary><h4><strong>Hint 3</strong></h4></summary>

Separate the two conditions with the `&` operator, because both conditions need to evaluate as true for the row to be included in the filtered dataframe.

</details>

# Conclusion

**What are your key takeaways from this lab?**

[Double-click here to record your response.]

**Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged. 

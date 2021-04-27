Readme
====

### Usage

```
main.py <intput_csv_filename> <output_csv_filename> <column_num_of_timestamp>
```
All the parameters are mandatory inputs.

column\_num\_of\_timestamp: The column whose value is the timestamp. The index starts from 0.

### Input csv format

The data downloaded from [https://data.binance.vision](https://data.binance.vision) or 
[https://github.com/binance/binance-public-data](https://github.com/binance/binance-public-data)

| trade Id | price | qty | quoteQty | time |isBuyerMaker | isBestMatch |
| -------- | ----- | --- | -------- | ---- | ----------- | ----------- |
| 51175358 | 17.80180000 | 5.69000000 | 101.29224200 | 1583709433583 |True|True|

Given a csv file `sample_input_file.csv` with the format above, the following is the command to know how many records are generated per hour. 

```
main.py sample_input_file.csv sample_output_file.csv 4

```

### Output csv format

| date and hour | line count  |
| ------------- |-------------|
| Mar-14-2021 03:00 | 86532 |
| Mar-14-2021 04:00 | 77225 |
| Mar-14-2021 05:00 | 73309 |

Each line count represents the number of records within 1 hour starting from the corresponding date and time. For example, the line count of the first row 86532 indicates the number of data rows from Mar-14-2021 03:00:00 to Mar-14-2021 03:59:59 in the source file.
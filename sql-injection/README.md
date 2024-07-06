```
author: 0xUu
date: July 6th, 2024
topic: SQL injection - pwa
```


# Lab: SQL injection UNION attack, determining the number of columns returned by the query

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

## Solution

the script I used is in `union-attack1.py`. Burpsuite needed another jdk version
which I didn't bother downloading, so I just used the requests module to make a request
to the url of the lab, open dev tools, see which requests are related to the category
where the vulnerability is mentioned, broke that down and tested how many columns
are present using `ORDER BY <number-of-column>--`, found that `category=Gifts`
contains **THREE** categories, I then solved the lab using the following injection:

```
<base-url>/filter?category=Gifts%27+UNION+SELECT+NULL%2C+NULL%2C+NULL--
```

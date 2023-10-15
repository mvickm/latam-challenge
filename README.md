**LATAM challenge**
==============================

# Summary

This file contains the information to install and run the program required by LATAM in this challenge.

A JSON file with an approximate data set of 398MBs is provided.  Tasks must be solved by implementing functions, one by approach (efficiency in time and efficiency in memory).

The following problems are addressed: 

1. The 10 best dates where there are more tweets. Mention the user (username) that more posts for each of those days. 

    It should include the following functions:
    ```
    def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    ```
    Returns:
    ```
    [(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
    ```


2. The 10 most commonly used emojis with their respective number. 
It must include the following functions:
    ```
    def q2_time(file_path: str) -> List[Tuple[str, int]]:
    def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    ```
    Returns:
    ```
    [("✈", 6856), ("❤", 5876), ...]
    ```

3. The 10 most influential users (username) in terms of mentions count (@) that records each of them. 
It must include the following functions:
    ```
    def q3_time(file_path: str) -> List[Tuple[str, int]]:
    def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    ```
    Returns:
    ```
    [("LATAM321", 387), ("LATAM_CHI", 129), ...]
    ```
# Installation

Before executing the main program I recommend you to create a virtual environment and install the 
required libraries.

```
python3 -m venv latam-challenge
source latam-challenge/bin/activate  
pip3 install -r requirements.txt
```
# Running

To run the main program execute the following command: 

```
python3 main.py --file_path [ruta_json]
```

If you want to monitor execution time, you can run the following command in a parallel console: 

```
py-spy top -- python3 main.py --file_path [ruta_json]
```
# Repository structure
------------

    ├── README.md          <- Code documentation
    │  
    ├── src
    │   └────solutions.py  <- Python file containing functions to calculate results optimized by time and memory
    │  
    ├── main.py            <- Main program 
    │     
    ├── request.py         <- Python file with request to POST results
    │        
    └──requirements.txt    <- Libraries required to run the main program

------------
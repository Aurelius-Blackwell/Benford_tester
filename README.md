# Benford_tester
This collection of programs can be used to test whether a group of files (placed together in a folder) adhere to Benford's Law. It can be used to identify an outlier among the files, i.e. to demonstrate that the file does not follow a numerical distribution from natural exponential processes.
To prevent periods or commas causing a simple regex to read one number as multiple numbers, the massEditor program first removes all periods and commas from the data.
The firstDigitCounter program can then read from the transformed data and lists the percentage frequency of each digit as a first digit within each file. These are saved to the benford_tests_template.xlsx file in the current working directory.
Finally, the benfordTest program performs a simple regression and adds the stats for each file to 

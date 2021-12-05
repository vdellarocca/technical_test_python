# technical_test_python
Rewriting in Python what was submitted in April


Some basic data quality checks are performed by the function in data_quality_checks_vdr.py. You do not need to run this function. It is automatically called when needed. It does:
1. Produce histograms to make it easy to assess for outliers.
2. Calculate the missing rate (expected to be very low if not null for gov data).
3. Calculate the zero rate.

The first code to run is 01_data_download.ipynb. This is what downloads the data. It does it in two different ways, just for exercise purposes:
1. By generalising the file and output name, to show how one could easily make it self-adjust for any future data release.
2. By dowloading directly from a link.
The code automatically creates a folder (if it does not exist already) where to store the data

The second code to run is 02_data_aggregation.ipynb. This code produces the final dataset by:
1. Loading all the Excel files. Note that similarly to what done in the previous code, one could generalise the file names. We have chosen not to, since it would be ta very similar exercise as what shown in the previous code.
2. Modify the column names, to allow for consistent notation.
3. Format the columns as needed.
4. Run the function in data_quality_checks_vdr.py, to check outliers, missing and zeros.
5. Create a series of dates, to use it as base to join all the datasets
6. Performs some other basics checks.
7. Performs some cleaning (e.g., filling any eventual missing values).
8. Join the dataframes, and creates the final dataset.




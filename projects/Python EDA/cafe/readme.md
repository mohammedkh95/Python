This is a dirty dataset I retrieved from Kaggle (https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training)

Its a simple dirty dataset solely to practice EDA using Pandas.
I used Visual Studio to do the cleaning using a Jyupiter file, pandas and numpy

The steps I undertook to clean it are:

1. I replaced all 'UNKNOWN' & 'ERROR' to "<NA>" values
2. Changed column data type since all of them where 'objects', some columns had to be changed to floats and date
3. I converted all the "<NA>" values to "Nan" because when trying to change certain columns to float, I would get an error.
4. The 'Total Spent' columns had values that where "NaN". To fix that issue, I just had to multiply the 'Quanity' by the 'Price Per Unit'.
5. I had to rename certain "NaN" values in the 'Item' columns. The website I got the dataset from has a list of prices for each item so I mapped some Items based on their Price Per Unit.
6. I dropped all the "NaN" values. No reason, just decided to go with it.
7. Converted to Excel

This was a simple project and my first. Trying to perfect Data Pre-processing before I move to EDA

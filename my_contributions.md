# My contributions

I have added the script to run the holehe process to all the mails contained in a CSV file.

## Files created

There are 3 files created:
1. ```main.py```
2. ```holehe_dataset.csv```
3. ```holehe_results.csv```

The ```main.py``` file takes the data from ```holehe_dataset.csv```, executes the process and creates the file ```holehe_results.csv``` with the results of the process in each e-mail.

### ```main.py```

I have refactored the script by splitting it into functions to improve modularity:

#### 🔹 **Cambios realizados**
1. **Separate functions** for each task:
   - `get_output_filename()`: Generates the name of the output file with the date.
   - `load_emails(file_path)`: Load the emails from the CSV.
   - `run_holehe(email)`: Run `holehe` on each mail and return the output.
   - `parse_results(email, lines)`: Filter and structure the results.
   - `save_results(results, output_file)`: Save the results in a CSV file.

2. **Main function `main()`**:
   - Loads the mails.
   - Executes `holehe` for each mail.
   - Process the results.
   - Saves the information in the CSV.

### `holehe_dataset.csv`

|First Name|Last Name|Email|
|----------|---------|-----|
|First|Test|test1@gmail.com|
|Second|Test|test2@gmail.com|

### `holehe_results.csv`

Shows the mailing and the site where the execution was positive

|Email|Sitio|[+]|
|-----|-----|---|
|test1@gmail.com|amazon.com|+|
|test1@gmail.com|bodybuilding.com|+|
|test1@gmail.com|eventbrite.com|+|
# Working with Files (File I/O)

The company you work with needs some modules in a bigger project for doing the following

- Performing IO operations on specifically 3 different files namely, Text, CSV and TSV files
- Reading rows from both CSV and TSV files

The relationship between these  files can be seen in the following ways

- Text, CSV and TSV files are types of files  
- CSV and TSV files are types of spreadsheets

In the bigger project, there exist two modules **ReadBytesFromFile** and **ProcessSpreadSheet** of which we do not know the actual implementation details of these modules, except for the signature and operations these modules expects to be performable on their respective argument.

**ReadBytesFromFile()**: This is a module that takes a file (either Text, CSV or TSV file) and can perform the following operations

- Treat the file object as a context manager, where on enter, the file is opened and then closed on exit.
- Treat the file object as an iterator which we can use to looping through lines in the file
- Read the complete content of the file at once.
- Read the first two lines of the file only.
- Read the last two lines only.

**ProcessSpreadsheet()**: This is a module that expects a spreadsheet, (either a CSV or TSV spreadsheet) as an argument and can perform the following operations

- Treat the spreadsheet object as an iterator for looping through the rows
- Iterate through the rows of the spreadsheet
- Read the complete content of the file
- Fetch only the first two rows of the spreadsheet
- Fetch only the last two rows of the spreadsheet

## Hints

- Treat a list of expected behavior above as contracts that the different files and spreadsheet respectively must comply to.
- The spreadsheet cannot be a type of file and vice versa because Text files cannot be treated as a spreadsheet.

### Important Notes

- The **ReadBytesFromFile** is not expected to know the kind of file it is taking in, it should just be able to perform all the expected operations on any file that comes in, same for ProcessSpreadsheet, it should not have an idea of whether the spreadsheet passed in is TSV or CSV.
- Opening files should manage its own context, that is opening the file and closing it afterwards. We do not want any close method in any of the modules.
- Handling CSV and TSV files should be done using Pandas DataFrame.
- Create a PR template of your choice into the .github folder to be used for PRs you will raise later
- Ensure to write unittest that covers at least 90% of your implementation
- When done and all tests are passing, raise a PR with a good title and body structure based on the content of the PR template you created at the beginning.

### What you will be practicalizing and will be used for reviews

- Understanding specification and asking timely questions where necessary.
- Breaking down large tasks into the smallest chunk of work
- Splitting a large module into components based on specification and understanding how to assemble these components to make up the whole usable module.
- Creating a good folder structure for module components.
- Strictly writing codes that comply with the SOLID principles.
- Understanding and using a third party library such as Pandas.
- Inheritance and Interface Polymorphisms.
- Iterators and generators
- Constructing a good inheritance hierarchy.
- Interfaces using abstract base classes.
- Unittest implementations

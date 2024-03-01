# SimCenter Documentation - User Inputs Documentation

Follow these steps to create documentation pages for the user inputs in the widgets of the SimCenter tools graphical interface:

## Step 1: Prepare Widget Header Files List

1. Add the names of the header files of the widgets you want to document to the file called `widget_header_files_list.txt`. This file is located at `SimCenterDocumentation/docs/common/user_manual/user_inputs_documentation`.

2. You can copy and paste the list of header files from the `.pro` or `.pri` files in the QtCreator project of the application you are developing.

3. It is okay to have duplicate entries in `widget_header_files_list.txt`; the Python script processing the file will automatically ignore duplicates.

4. If you want to exclude specific entries from processing, add a `#` before the text on those lines in `widget_header_files_list.txt`.

## Step 2: Create Starter CSV Files

1. Open a terminal/command window.

2. Navigate to the location of the "SimCenterDocumentation" repository on your system.

3. Run the command `make starter_files`.

4. This will create CSV files in the directory `User_Inputs_Documentation_CSV_Files`, which is located under `SimCenterDocumentation/docs/common/user_manual/user_inputs_documentation`.

5. These CSV files will only contain the header row.

## Step 3: Fill Out CSV Files

1. Open the starter CSV files created in the previous step.

2. Fill in the documentation content, providing one row for each user input item in the widget.

## Step 4: Generate RST Files

1. Once the CSV files are prepared, navigate to the location of the "SimCenterDocumentation" in your terminal/command window.

2. Run the command `make user_inputs`.

3. This will generate RST files in the directory `User_Inputs_Documentation_RST_Files`, located under `SimCenterDocumentation/docs/common/user_manual/user_inputs_documentation`. These RST files will be created using the content from the CSV files in `User_Inputs_Documentation_CSV_Files`.

4. Additionally, this command will update the contents of the file `User_Input_Documentation_Tables.rst`, which is located in `SimCenterDocumentation/docs/common/user_manual/user_inputs_documentation`.

## Step 5: Build Documentation

1. Run the usual command to build the documentation pages, such as `make qfem html`, in the terminal/command window at the location of the "SimCenterDocumentation" repository on your machine.


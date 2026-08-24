# This is Day 44 project : Data Cleaner

import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        if file_path.lower().endswith(".csv"):
            df = pd.read_csv(file_path)

        elif file_path.lower().endswith((".xlsx", ".xls")):
            df = pd.read_excel(file_path)

        else:
            print("Unsupported file format.")
            print("Please use a CSV or Excel file.")
            return None

        print("\nData loaded successfully!")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        return df

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("Error loading data:", e)
        return None
    
def handle_missing_values(df):
    """Allow the user to choose how to handle missing values."""
    missing_count = df.isnull().sum().sum()
    if missing_count == 0:
        print("\nNo missing values found.")
        return df
    print(f"\nMissing values found: {missing_count}")

    print("\nHow do you want to handle missing values?\n")
    print("1. Drop rows containing missing values")
    print("2. Fill missing values")

    choice = input("\nEnter your choice (1-2): ").strip()

    if choice == "1":
        initial_rows = len(df)
        df = df.dropna()
        removed_rows = initial_rows - len(df)
        print(f"\n{removed_rows} row(s) removed because of missing values.")

    elif choice == "2":
        numeric_columns = df.select_dtypes(include="number").columns
        text_columns = df.select_dtypes(include="object").columns

        for column in numeric_columns:
            if df[column].isnull().any():
                df[column] = df[column].fillna(df[column].median())

        for column in text_columns:
            if df[column].isnull().any():
                df[column] = df[column].fillna("Unknown")
                
        print("\nMissing values filled successfully.")
        print("Numeric columns → Median")
        print("Text columns → Unknown")
    else:
        print("Invalid choice.")
        print("Keeping missing values unchanged.")
    return df

def rename_columns(df):
    """Allow the user to rename columns interactively."""
    print("\n------ Rename Columns ------")
    print("\nCurrent columns:")
    for index, column in enumerate(df.columns, start=1):
        print(f"{index}. {column}")

    choice = input("\nDo you want to rename any columns? (y/n): ").strip().lower()

    if choice != "y":
        return df

    while True:
        print("\nCurrent columns:")
        for index, column in enumerate(df.columns, start=1):
            print(f"{index}. {column}")

        column_number = input("\nEnter column number to rename (or 'done' to finish) : ").strip()
        if column_number.lower() == "done":
            break

        try:
            column_number = int(column_number)
            if not 1 <= column_number <= len(df.columns):
                print("Invalid column number.")
                continue
            old_name = df.columns[column_number - 1]
            new_name = input(f"Enter new name for '{old_name}': ").strip()

            if not new_name:
                print("Column name cannot be empty.")
                continue
            if new_name in df.columns:
                print("A column with this name already exists.")
                continue

            df.rename(columns={old_name: new_name}, inplace=True)
            print(f"'{old_name}' renamed to '{new_name}'.")
        except ValueError:
            print("Please enter a valid column number.")
    return df

def remove_duplicates(df):
    """Remove duplicate rows."""
    print("\n------ Removing Duplicates ------")
    duplicate_count = df.duplicated().sum()
    if duplicate_count == 0:
        print("No duplicate rows found.")
        return df
    df = df.drop_duplicates()
    print(f"\n{duplicate_count} duplicate row(s) removed.")
    return df
    
def clean_data(df):
    """Clean the dataset."""
    print("\n================================")
    print("        CLEANING DATA")
    print("================================")
    print(f"\nInitial Shape : {df.shape}")
    
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = rename_columns(df)
    
    print("\n------ Cleaning Complete ------")
    print(f"Final Shape: {df.shape}")
    return df

def save_data(df, output_path):
    """Save the cleaned data to a new CSV or Excel."""
    try:
        if output_path.lower().endswith(".csv"):
            df.to_csv(output_path, index=False)
        elif output_path.lower().endswith((".xlsx", ".xls")):
            df.to_excel(output_path, index=False)
        else:
            print("Unsupported output format.")
            print("Use .csv or .xlsx")
            return
        print(f"\nCleaned data saved successfully to : {output_path}")
    except Exception as e:
        print("Error saving data:", e)
        
def main():
    print("\n================================")
    print("       DATA CLEANER TOOL")
    print("================================")

    print("\nSupported files:")
    print("• CSV (.csv)")
    print("• Excel (.xlsx / .xls)")
    
    input_file = input("\nEnter the path to your file : ").strip()
    df = load_data(input_file)
    if df is None:
        return
    
    print("\n------ Initial Data ------\n")
    print(df.head())
    
    print("\n------ Missing Value Summary ------")
    print(df.isnull().sum())
    
    df = clean_data(df)
    
    print("\n------ Cleaned Data ------")
    print(df.head())
    
    output_file = input("\nEnter the path to save the cleaned file : ").strip()
    save_data(df, output_file)
    
if __name__ == "__main__":
    main()
    
# Done
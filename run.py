import gspread
from google.oauth2.service_account import Credentials

# Provide the absolute path to the creds.json file
creds_file_path = 'C:\\Users\\marie\\OneDrive\\Documents\\vscode-projects\\Love_Sandwiches_Project\\creds.json'

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


# Authenticate and authorize
CREDS = Credentials.from_service_account_file(creds_file_path)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Access the Google Sheet by its name
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


# Function to get sales data
def get_sales_data():

    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

# Call the function


get_sales_data()

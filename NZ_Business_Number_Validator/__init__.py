import re


# This method will take the passed NZBN string
# remove all non-numeric characters
def clean_nzbn(nzbn):
    # Use regex to remove all non-numeric characters
    clean_nzbn_number = re.sub('[^0-9]', '', str(nzbn))

    # Returns the "clean" NZBN number
    return str(clean_nzbn_number)


# This method will take the passed NZBN number
# and use the set validation process to determine
# whether the IRD is valid or invalid
def is_valid(nzbn):
    # For "safety" reasons use the clean method to make sure
    # the NZBN number only contains numerical characters before
    # validating
    nzbn_to_validate = clean_nzbn(nzbn)

    # Check that the NZBN is the correct length and
    # that the first character is a 9
    if len(nzbn_to_validate) == 13 and nzbn_to_validate[0] == "9":
        # If both of them are True then the NZBN Number is valid
        return True

    # Return False by default
    return False

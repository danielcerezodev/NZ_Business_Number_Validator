# New Zealand Business Number Validator
Python package that consumes a NZBN and returns either True or False depending on whether the NZBN Number is valid or not.

## Getting Started

These instructions will get you a copy of the project up and 
running on your local machine for development and testing purposes.

If you would like to create your own package follow the guide below:
* [Packaging project](https://packaging.python.org/tutorials/packaging-projects/)

## Installing

```
pip install git+https://github.com/danielcerezodev/NZ_Business_Number_Validator.git
```

## Usage

```
from NZ_Business_Number_Validator import is_valid

nzbn_number = "9876543210123"

is_nzbn_number_valid = is_valid(nzbn_number)

if is_nzbn_number_valid:
    print(nzbn_number + " is valid")
else:
    print(nzbn_number + " is not valid")
```

## How the validation is done

The following steps are performed:

* Check the valid amount of digits
    * If the NZBN does not contain exactly 13 digits the number is invalid.
* Check the leading digit
    * If the first digit of the NZBN is NOT a 9, the number is invalid.

## Built With

* [Python](https://www.python.org/) - Programming language
* [Pycharm](https://www.jetbrains.com/pycharm/) - IDE

## [Changelog](https://github.com/danielcerezodev/NZ_Business_Number_Validator/blob/master/CHANGELOG.md)

## Contributing

Pull requests are welcome.

## Authors

* [**Daniel Cerezo**](https://github.com/danielcerezodev)

## License

This project is licensed under the GNU License - see the [LICENSE.md](https://github.com/danielcerezodev/NZ_Business_Number_Validator/blob/master/LICENSE.md) file for details.

# Excel-to-Image-Converter

This is a Flask application that converts Excel files to images.

## Installation

To install the application, clone the repository and install the dependencies:

```shell
git clone <repository URL>
cd <repository name>
pip install -r requirements.txt
```

## Usage
To use the application, send a POST request to the /convert endpoint with an Excel file attached. The application will convert the file to an image and return it as a PNG file.
```shell
curl -X POST -F "file=@<path to Excel file>" <application URL>/convert
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.  
I hope this helps!

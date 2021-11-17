####Thesis for the test automation with Selenium and Python course


#### Executable commands:

Run test which need to review
```bash
pytest -v --tb=line --language=en -m need_review
```
Run all tests for main page
```bash
pytest -v --tb=line --language=en test_main_page.py
```
Run all tests for product page
```bash
pytest -v --tb=line --language=en test_product_page.py
```
Also, you can change site language for check universality tests. For this you need set language from list:
```bash
--language=language from the list
```
####List of languages:
* **en** - _English_
* **ru** - _Russian_
* **es** - _Spanish_
* **fr** - _France_
* **de** - _German_
* **pl** - _Poland_
#### To work for executable commands you need:
* Download chromedriver94 - https://sites.google.com/a/chromium.org/chromedriver/downloads
* Put chromedriver.exe in the specified path - **C:\chromedriver**
* Add path to the folder with the driver in the system variable - https://www.computerhope.com/issues/ch000549.htm
* Reset your device

#### Stack:
* Python 3.8+
* Selenium 3.14
* Pytest 5.1

#### Python requirements:
`requirements.txt`

Installation of requirements:
```bash
pip3 install -r requirements.txt
```

#### Developers:
Shkvalik
`valikko2004@gmail.com`

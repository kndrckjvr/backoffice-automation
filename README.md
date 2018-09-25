# SETUP_TEST_ENVIRONMENT_SELENIUM_WEBDRIVER_LINUX

* Operating System Name: Lubuntu 16.04 64-bit

## A. INSTALLING PYTHON
```
sudo apt-get update
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd /usr/src
sudo wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz
sudo tar xzf Python-2.7.14.tgz
cd Python-2.7.14
sudo ./configure --enable-optimizations
sudo make altinstall
python2.7 -V
```
Result:
```
Python 2.7.14
```
## B. INSTALL CHROMEDRIVER

```
cd /usr/local/bin
wget -N https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver
```

## C. INSTALL SELENIUM
```
sudo apt-get install python-pip
sudo pip install selenium
```

## D. INSTALL VISUAL STUDIO CODE
```
wget -N https://az764295.vo.msecnd.net/stable/f46c4c469d6e6d8c46f268d1553c5dc4b475840f/code_1.27.2-1536736588_amd64.deb -P ~/
sudo dpkg -i code_1.27.2-1536736588_amd64.deb
sudo apt-get install -f
rm ~/code_1.27.2-1536736588_amd64.deb
```

# Windows 10

* Operating System Name: Windows 10 64-bit


## A. INSTALL PYTHON 2.7.14
```
Download
https://www.python.org/ftp/python/2.7.14/python-2.7.14.amd64.msi
Open then Click Next until the setup ends

Setup python for cmd

Press Windows Key + S (Search)
Type and Click "View Advanced System Settings"

Then Click "Environment Variables..."

Edit "Path" Variable

if a dialog pop-up with a list of paths
Press New then input "C:/Python27" (without the "")

if a dialog pop-p with a list of paths separated with semi-colons (;)
Input "C:/Python27;" (without the "")

Press Ok until System Properties is closed.

Press Windows + R input "cmd"
Type in "python --version"
Output: Python 2.7.14 
```

## B. INSTALL CHROME DRIVER
```
Download
https://chromedriver.storage.googleapis.com/2.42/chromedriver_win32.zip
Extract to "C:/User/<computer-name>"

Setup Chrome Driver for cmd

Press Windows Key + S (Search)
Type and Click "View Advanced System Settings"

Then Click "Environment Variables..."

Edit "Path" Variable

if a dialog pop-up with a list of paths
Press New then input "C:/Users/<computer-name>/chromedriver_win32" (without the "")

if a dialog pop-p with a list of paths separated with semi-colons (;)
Input "C:/<computer-name>/chromedriver_win32;" (without the "")

Press Ok until System Properties is closed.

Press Windows + R input "cmd"
Type in "chromedriver"
Output: 
Starting ChromeDriver 2.42.591088 (numbers) on port (portnumber)
Only local connections are allowed.

Press Ctrl + C to exit
```

## C. INSTALL SELENIUM

```
Press Windows + R input "cmd"
Type in "C:\Python35\Scripts\pip.exe install selenium"

Output:
Collecting selenium
  Downloading https://files.pythonhosted.org/packages/b0/c9/52390baa8d6b65c3e3b89f522c3a0fcf58f2b4faf37893ef9d97cddde699/selenium-3.14.1-py2.py3-none-any.whl (902kB)
    100% |################################| 911kB 312kB/s
Collecting urllib3 (from selenium)
  Downloading https://files.pythonhosted.org/packages/bd/c9/6fdd990019071a4a32a5e7cb78a1d92c53851ef4f56f62a3486e6a7d8ffb/urllib3-1.23-py2.py3-none-any.whl (133kB)
    100% |################################| 143kB 541kB/s
Installing collected packages: urllib3, selenium
Successfully installed selenium-3.14.1 urllib3-1.23
You are using pip version 9.0.1, however version 18.0 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
``` 

## D. INSTALL VISUAL STUDIO CODE
```
Download
https://aka.ms/win32-x64-user-stable

Click Next until setup ends
```
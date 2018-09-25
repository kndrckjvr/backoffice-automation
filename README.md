# SETUP_TEST_ENVIRONMENT_SELENIUM_WEBDRIVER_LINUX

* Operating System Name: Lubuntu 16.04
* Type: 64-bit


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

## D. INSTALL VSCODE
```
wget -N https://az764295.vo.msecnd.net/stable/f46c4c469d6e6d8c46f268d1553c5dc4b475840f/code_1.27.2-1536736588_amd64.deb -P ~/
sudo dpkg -i code_1.27.2-1536736588_amd64.deb
sudo apt-get install -f
rm ~/code_1.27.2-1536736588_amd64.deb
```
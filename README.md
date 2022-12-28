# QA_diploma 

To run tests:

1. Copy the repository via SSH.
2. Download chromedriver for your operating system and the appropriate version and put it in the PATH variable.
3. Create a virtual environment and log in to it(Windows: python -m venv venv, venv/Scripts/activate;
Linux: python3 -m venv venv, source venv/bin/activate)
4. Download all modules to the virtual environment (pip3 install -r requirements.txt)
5. Install Allure, installation documentation:
    Windows: https://docs.qameta.io/allure-report/#_installing_a_commandline
https://github.com/ScoopInstaller/Scoop
    Linux: wget https://github.com/allure-framework/allure2/releases/download/2.19.0/allure-2.19.0.tgz
sudo tar -zxvf allure-2.19.0.tgz -C /opt/ 
sudo ln -s /opt/allure-2.19.0/bin/allure /usr/bin/allure
OpenJDK installation documentation
    Windows: https://learn.microsoft.com/ru-ru/java/openjdk/download
https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/
    Linux: sudo apt install default-jre -y
6. The tests are run by the command pytest -v --alluredir=../report
7. View allure report allure serve ../reports
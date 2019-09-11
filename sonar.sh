coverage erase
nosetests --with-coverage --with-xunit
coverage xml
sonar-scanner
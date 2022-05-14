rem python -m pytest  -v -m "sanity"  --html=C:\Selenium\vkcom\vkcom_pytest\reports\report.html C:\Selenium\vkcom\vkcom_pytest\testCases\ --browser Chrome
python -m pytest  -v -m "regression"  --html=C:\Selenium\vkcom\vkcom_pytest\reports\report.html C:\Selenium\vkcom\vkcom_pytest\testCases\ --browser Chrome
rem python -m pytest  -v -m "uat"  --html=C:\Selenium\vkcom\vkcom_pytest\reports\report.html C:\Selenium\vkcom\vkcom_pytest\testCases\ --browser Chrome
rem python -m pytest  -v -m "uat and sanity"  --html=C:\Selenium\vkcom\vkcom_pytest\reports\report.html C:\Selenium\vkcom\vkcom_pytest\testCases\ --browser Chrome
rem python -m pytest -v  --html=C:\Selenium\vkcom\vkcom_pytest\reports\report.html C:\Selenium\vkcom\vkcom_pytest\testCases\test_FindUser.py --browser Chrome
rem python -m pytest  -v -m "test"  --html=C:\Selenium\vkcom\vkcom_pytest\reports\report.html C:\Selenium\vkcom\vkcom_pytest\testCases\ --browser Chrome







pause
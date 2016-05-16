from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://booksbunker.com/search/%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%20%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD/")
lastElement = driver.find_element_by_xpath("//div[@class='pagination']//ul//li[last() - 2]").text

i = 1
listNamesAll = []
listAuthorsAll = []
listUrlAll = []
while i <= int(lastElement):
    driver.get("http://booksbunker.com/search/%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%20%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD/" + str(i) + ".html")
    listNames = driver.find_elements_by_xpath("//div[@class='span9']//h3//a[not(@class)]")
    listAuthors = driver.find_elements_by_xpath("//div[@class='span9']//h3//small")
    i += 1
    for element in listAuthors:
        listAuthorsAll.append(element.text)
    for element in listNames:
        listUrlAll.append(element.get_attribute("href"))

for element in listUrlAll:
    driver.get(element)
    name = driver.find_element_by_xpath("//div[@class='span9']//div[@class='page-header']//h1//span[not(@class)]").text
    listNamesAll.append(name)

for element in listNamesAll:
    print element

for element in listAuthorsAll:
    print element

for element in listUrlAll:
    print element

driver.close()

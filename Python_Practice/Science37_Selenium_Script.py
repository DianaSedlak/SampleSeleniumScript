from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver =webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# This is my first cover letter in code 
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter the name of a really close startup that could save the lives of those I love, and it could also blend my past of dropping out of grad school for Occupational Therapy with my last three years of software testing and tinkering with technology and mobile. Did I mention this cuts my current commute in half? Woohooo I could walk to work! Wait do they have onsite showers? So not professional, but this script is.
search_field.send_keys("Science 37")
search_field.submit()

# See how awesome and close Science 37 is, but whats with the 984 phone number?
# By geting the list of elements which are displayed after the search
#currently on result page using find_elements_by_class_name method
lists=driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists))+ "searches;")

# iterate through each element and print the text... Wait wow impressive Series B round!

i=0
for listitem in lists:
    print (listitem)
    i=i+1
    if(i>10):
       break

#close the browser window and hope this is a decent cover letter
driver.quit()
 

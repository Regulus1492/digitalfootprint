# **Basic Digital Footprint Checker**

### **Video Demo:**


### **Description:**


#### **Motivation**

Technology is as widespread as ever. Every year more people navigate the internet using multiple devices. However, all this connectivity comes at a cost. The cost of privacy. When we use the internet, we leave footprints behind. 
Footprints are stored seamlessly by the services we use. A lot of this information is freely available and can be systematically extracted. The issue arises if this information falls into the wrong hands. Scammers and unethical hackers might use this information to harm naive users. 

This project aims to raise awareness on the issue by showing the user his or her digital footprint, from two popular sources; namely, Google searches and Radaris. 


#### **Program description**


The project consists of a basic command-prompt python-program that shows the digital footprint of the user that interacts with it. 

I mine the user's digital footprint data using web scraping techniques tailored towards Google searches and Radaris. For instance, for Google searches: I use a method to format the user's input into a google search query, which is fetched from Google. Then I get access to the contents of the first page of the Google search (the code does not allow for pagination -- perhaps I should work on it some other time). I am interested in the links fetched by the search, and some additional information such as the title of the page, the link associated to it, and some text associated to it. 

I want the user to have a compact glimpse of the sort of information that a search engine may produce if the user places her name on a google search. I stored all this information in a dictionary. I do it for simplicity, just because I do not have time to place all this information in a structured database. 

As for Radaris, not as common as Google, it is a web page that looks for available information given a user's name. The information ranges from name coincidences, relatives and addresses. As far as I understand, information is from the United States only. Radiris is a bit harder to web scrape, since its content is dynamic. That is why I use BeautifulSoup library. Then I had to access the HTML using Chrome DevTools to find the names of the classes and methods that stored the information of interest. In this case I went for name and address. I collapsed the information into a zip element for time constraints.  Then I store the zip element in a dictionary. 

Both results from Google and Radaris are stored into a dictionary and printed after an introductory message. 


#### **Content**

The project contains the following files and documents: 

- src: a file that contains experimental scripts that helped built the final version of the program
- digitalfootprintchecker.py: this is the script that runs the program and calls the other scripts. 
- error_handling.py: the script contains functions that deal with possible unwanted entries such as digits or special characters in the inputs. 
- googlemining.py: contains the functions that allow the program to web scrap from a Google search page. 
- radarismining.py: contains the functions that allow the program to web scrap from Radaris. 
- intromessage.py: procures a greeting message for the user. 


#### **How to use**

In the prompt after the path type: `python3 digitalfootprintchecker.py --first_name [FIRST_NAME] --last_name [LAST_NAME]`  and replace `[FIRST_NAME]` and `[LAST_NAME]` with the desired first name and last name. If you want to place either two first names or  last names do so with quotes. Eg. “name1 name2”. 


#### **Sources**

- [How to search and find your digital footprint](https://blog.tdstelecom.com/security/how-to-search-and-find-your-digital-footprint/)
- [How to scrape google search results using Python](https://practicaldatascience.co.uk/data-science/how-to-scrape-google-search-results-using-python)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


### **Author**
[Check my Linkedin page](https://www.linkedin.com/in/juan-carlos-serrano-mera/)

# Basic Digital Footprint Checker
#### Video Demo:
#### Description:

##### Motivation

##### Program description


The project consist of a basic command-prompt python-program that shows the digital footprint of the user that interact with it. 

The user's digital footprint is mined using web scraping techniques tailored towars Google searches and Radaris. For instance, 
for Google searches: I use a method to format the user's input into a google search query, which is fetched from Google. Then I get access to the contents of the first page of the Google search (the code does not allow for pagination -- perhaps I should work on it some other time). I am interested on the links fleched by the search, and some additional information such as as the title of the page, the link associated to it, and some text associated to it. 

I want the user to have a compact glimpse of the sort of information that a search engine may produce if the user places her name on a google search. I store all this information into a dictionary. I do it for simplicity, just be cause I do not have time to place all this information in a proper structured data base. 

As for Radaris, not as common as Google, it is a web page that looks for available information give a user's name. The information ranges from name coincideces, relatives and addressess. As far as I understand, information is from the United States Only. Radiris is a bit harder to web scrape, since its content is dynamic. That is why I use BeautifulSoup library. Then I had to access the HTML using Chrome DevTools to get the information I wanted to extract. In this case I went for name and address. I collapsed the iformation into a zip element for time constraints. 

Both results from Google and Radaris are stored into a dictionary and printed after a introductory message. 


##### Content

The project cotains the following files and documents: 

- src: a file that contains experimental scripts that helped built the final version of the program
- digitalfootprintchecker.py: this is the sript that runs the program, and calls the other scripts. 
- error_handling.py: the script contains functions that deal with possible unwanted entries such as digits or special charaters in the inputs. 
- googlemining.py: containst the functions that allow the program to web scrap from a Google search page. 
- radarismining.py: containst the functions that allow the program to web scrap from Radaris. 
- intromessage.py: procurs a greeting message for the user. 

##### Sources

On digital footprint

On web scrapping

Other topics
TO DO 
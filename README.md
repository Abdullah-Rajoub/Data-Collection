# Data-Collection
This script needs only links to websites, then it gets the data from the websites, and generated objects that have prompt, completion, URL, data types and the data of when this script was run. Then the scripts write all the objects generated into a file called test.json.
You need to run the script from a file called web_scrapper.py. Before running it, you have to update the "url" array in web_scrappers.py to the urls of the websites you want to extract data from. Also, when you run it, you need to provide the "Data Type" field for each URL (Meta data you asked to add to json). Also, there is a minute of waiting between two consecutive requests to the Open AI API, so it doesn't get blocked, because Open AI API has a 3 request per minute policy.
Also you need to use your own Open AI API key. This key used in the code has been disabled. 

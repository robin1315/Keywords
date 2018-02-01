## Keywords Counter
Simple web application written to count keywords on the website in Flask. 
Using Python 3, BeautifulSoup4 library use to parse, WTForm to create form.

The application prossesing url address, get all keywords found in ```<meta>``` tags with an attribute equal to ```"keywords"``` (no matter case) size and counts their number on the page.


## How use
1. Clone repository ```git clone https://github.com/robin1315/Keywords.git```
2. Install the required libraries using e.g. ```pip install -c .\requirements.txt```
3. Run ```python run.py```
4. Open your browser and enter address ```http://127.0.0.1:5000/```
5. In the form field enter URL
6. Press check button




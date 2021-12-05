# SLASH PHASE 3

## Motivation:
Slash was envisioned as a console application which was meant to be used as a standalone native Python desktop application. Even though a native application is good in usecases such as heavy processing and zero downtime but in the bigger picture, it fades in comparison to an online web application. Our efforts in phase-II were to convert a native desktop Python application to a web application(APIs) and expand the horizon by bringing in more e-commerce websites support as well as support for API calls to sites that don't support scraping. Our vision is to provide a one-stop abstraction for all web scraping needs which is packaged in a sleek and easy to implement cloud pipeline. Integrating CI/CD to our API was crucial to our goal as we believe the next phase should not dwell in the past but rather focus on the future. 

## Introduction:
Slash is a publicly accessible web API framework that allows one to scrape the most popular e-commerce websites to get the best deals on the searched items across multiple e-commerce websites. Currently supported websites include [Amazon](https://www.amazon.com/), [Walmart](https://www.walmart.com/), [Target](https://www.target.com/), [BestBuy](https://www.bestbuy.com/), [Costco](https://www.costco.com/) and [EBay](https://www.ebay.com/).
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash introduces easy to use public APIs to filter, sort and search through the search results
- **Powerful**: Produces JSON responses that can be easily customised to bring about the desired output

## Steps for Execution
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/rohan22shah/slash-phase3.git
cd slash
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip3 install -r requirements.txt
```
4. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the python command to run the ```main.py``` file.
```
cd src

For Mac
python3 main.py

For Windows
python main.py
```
5. To run streamlit application
```
streamlit run slash_user_interface.py
```

## Technology Used
---
- Streamlit [https://streamlit.io/]
- Android Studio
- Python


## Output

The below Images shows the android application developed for Slash Phase 3
<img src = 'https://github.com/rohan22shah/slash-phase3/blob/main/media/App_1.png'>
<img src = 'https://github.com/rohan22shah/slash-phase3/blob/main/media/App_2.png'>
<br>
The below images shows the websites developed for Slash Phase 3
<img src = 'https://github.com/rohan22shah/slash-phase3/blob/main/media/Website_1.png'>
<img src = 'https://github.com/rohan22shah/slash-phase3/blob/main/media/Website_2.png'>

<p align="center"><img width="500" src="./assets/slash.png"></p>

![GitHub](https://img.shields.io/github/license/Urvashi74/slash)
![github workflow](https://github.com/secheaper/cheaper/actions/workflows/python-app.yml/badge.svg) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5646505.svg)](https://doi.org/10.5281/zenodo.5646505)
![Github](https://img.shields.io/badge/language-python-red.svg)
![GitHub issues](https://img.shields.io/github/issues-raw/Urvashi74/slash)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/Urvashi74/slash)
![Github pull requests](https://img.shields.io/github/issues-pr/Urvashi74/slash)
![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/Urvashi74/slash)

Do you love shopping? Are you in search of some good deals while shopping online?! Slash is here to help you look for the best deals!


Slash is a publicly accessible web API framework that allows one to scrape the most popular e-commerce websites to get the best deals on the searched items across multiple e-commerce websites. Currently supported websites include [Amazon](https://www.amazon.com/), [Walmart](https://www.walmart.com/), [Target](https://www.target.com/), [BestBuy](https://www.bestbuy.com/), [Costco](https://www.costco.com/) and [EBay](https://www.ebay.com/).
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash introduces easy to use public APIs to filter, sort and search through the search results
- **Powerful**: Produces JSON responses that can be easily customised to bring about the desired output

---

:rocket: Improvements over Phase-I
---

Slash was envisioned as a console application in Phase-I which was meant to be used as a standalone native Python desktop application. Even though a native application is good in usecases such as heavy processing and zero downtime but in the bigger picture, it fades in comparison to an online web application. Our efforts in phase-II were to convert a native desktop Python application to a web application(APIs) and expand the horizon by bringing in more e-commerce websites support as well as support for API calls to sites that don't support scraping. Our vision is to provide a one-stop abstraction for all web scraping needs which is packaged in a sleek and easy to implement cloud pipeline. Integrating CI/CD to our API was crucial to our goal as we believe the next phase should not dwell in the past but rather focus on the future. Below is the breakdown of step by step improvement and our reasoning behind the same:
1) Web Scraper Extension: Added additional websites to the scraper logic. Even though the earlier scraper was targeting popular sites like Amazon and Walmart, we all know that the more the merrier. So, we integrated Target, CostCo, eBay and BestBuy to our scraper logic which enabled us to provide more options to the users.
2) Web APIs: We created a web API to access internal scraper logic in a streamlined manner. Using a single path, all the different e-commerce sites can be scraped and results can be obtained. We believe that creating an API for scraper code was the next logical step for expanding the usecase of our application.
3) Export functionality: Using the same link to access our scraper web API and sending the optional parameter export=True, generates a csv file of our results. This file can directly be worked upon by other applications or can be used to drive the business logic.
4) Uvicorn Server: We used a lightweight ASGI(Asynchronous Server Gateway Interface) server called the Uvicorn server. This server enables us to quickly host the fastAPI APIs in a quick and seamless way.
5) Cloud: Our next step involved the conversion from a local web application to a cloud application to ensure no downtime and complete availability. We deployed the API onto cloud (Microsoft Azure) and enabled CI/CD using Github Actions. Docker was used as a container to run our uvicorn server. We then deployed Dockerised services on Azure. Extensive documentation to the same is provided in the [Github Actions-Azure Integration.pdf](https://github.com/Urvashi74/slash/blob/main/docs/Github%20Actions-Azure%20Integration.pdf) file in the docs folder.
---
<p align="center">
  <a href="#movie_camera-checkout-our-video">Checkout our video</a>
  ::
  <a href="#rocket-installation">Installation</a>
  ::
  <a href="#computer-technology-used">Technology Used</a>
  ::
  <a href="#bulb-use-case">Use Case</a>
  ::
  <a href="#file_cabinet-api">API</a>
  ::
  <a href="#page_facing_up-why">Why</a>
  ::
  <a href="#golf-future-roadmap">Future Roadmap</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
  ::
  <a href="#email-support">Support</a>
  
</p>

---

:movie_camera: Checkout our video
---

https://user-images.githubusercontent.com/25104264/140454029-315ceada-ffe1-434a-bad6-3c1f389a7795.mp4

---

:rocket: Installation
---
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/secheaper/slash.git
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

:computer: Technology Used
---
- FastAPI : https://fastapi.tiangolo.com
- ASGI Server - Uvicorn : https://www.uvicorn.org
- Docker : https://www.docker.com
- Azure : https://azure.microsoft.com/en-us/


:bulb: Use Case
---
* ***Students***: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
* ***Data Analysts***: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually inportant.


:file_cabinet: API
---
## Documentation

Documentation can be accessed anytime via the below link.
 
	 `https://slash-app-staging.azurewebsites.net/`

## Search Items Api

Wrapper API to fetch slash scrape results. This API provides a one step solution to access scrape results from all our integrated websites.

    https://slash-app-staging.azurewebsites.net/{site}/{item_name}

**Required parameters:**

 - **site**: *az* for amazon; *wm* for walmart; *eb* for ebay; *cc* for costco; *tg* for target and *bb* for bustbuy. Alternatively '*all*' in site can be used to get results for all sites.
    
 - **item_name**: items to be searched by slash web api; *examples below*

`https://slash-app-staging.azurewebsites.net/az/toys`

`https://slash-app-staging.azurewebsites.net/all/dell`

**Optional parameters**

- **relevant**: string relevance: items will be ordered by relevance. Not supported currently.
- **order_by_col**: string column_name: items will be ordered by the column name. Currently only the 'price' column ordering is supported.
- **reverse**: boolean val: items will be displayed in the same or the opposite order based on the value of this parameter.
- **listLengthInd**: integer len(default value is 10): sets the upper limit on the number of entries that will be displayed
- **export**: boolean val(default value is false): items can be exported in a csv file;; *examples below*

`https://slash-app-staging.azurewebsites.net/all/dell?export=false&listLengthInd=5&order_by_col=price&reverse=false`

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!
- Slash in its current form is for students who wish to get the best deals out of every e-commerce site and can be used by anyone who is willing to develop an application that consumes these web APIs.
- Future scope includes anything from a web application with a frontend or any Android or IOS application that utilises these Web APIs at their backend. Anyone can build their own custom application on top of these web APIs.

:golf: Future Roadmap
---
- Our API can be used by end users such as developers who are tech-savvy individuals looking to get a one stop solution for web scraping ecommerce websites such as Amazon, Target, Ebay,etc along with API access to multiple ecommerce websites. It'll be available directly for access to people without having to dive deep into the code.
- Front End implementation of Slash API , ie., converting it into a full stack web application.
- Chrome Extension using the functionalities of Slash API
- An iOS app or Android application.

:sparkles: Contributors
---
* [Anirudh Pande](https://github.com/apande95)
* [Bradley Erickson](https://github.com/bradley-erickson)
* [Lalit Bangad](https://github.com/lalit10)
* [Pratyush Vaidya](https://github.com/Pratyush1184)
* [Urvashi Kar](https://github.com/Urvashi74)

:email: Support
---
For any queries and help, please reach out to us at: slashcsc510@gmail.com

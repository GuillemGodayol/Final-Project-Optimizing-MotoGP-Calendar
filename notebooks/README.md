<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Optimizing MotoGP Calendar. A TSP based approach.
*Guillem Godayol*

*Data Analytics. Ironhack Barcelona. October 2019*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
In this project I tried to optimize the route from circuit to circuit on the MotoGP 2020 Season Calendar.

The aim of the project is to work with algorithms to approach the Travelling Salesman Problem, which is a problem that can be applied on different situations on daily business based on logistics, mobility and sales.

## Hypotheses / Questions
* The main hypotesis is that the travelled distance can be reduced more than 25% optimizing the order of the circuits to visit.

## Dataset
* The data about the circuits and dates was scaped from the official MotoGP site: www.motogp.com using BeautifulSoup Scraper.
* From the same site I scraped information about the riders for further improvements.
* After getting the information, I complemented it with the coordinates for each circuit and hometown for riders using GeoPy Library.


## Cleaning
The cleaning part was basically focused on checking for non repeated values and coordinates, as the scraped data had no null values. For some very specific cases I need to make some manually cleaning.

## Analysis
* The first step of the analysis was making clusters of the circuits using two different unsupervised learning algorithms: DBSCAN and KMeans.
* Whit clusters being defined, next step was apply MLRose Algorithm to get an approach to the optimized route for each cluster, taking into account that those were round routes.
* The final step was to check the circuits closest to other clusters, 'open' the routes on those circuits, and calculate the distance from one to another to get the whole distance.

## Model Training and Evaluation
* As I used Unsupervised Learning models, they don't need to be trained.
* My features were just two: Latitude and Longitude, so the best way to evaluate the obtained results was plotting the clusters into a map and see if those results made sense or not.

## Conclusion
* I got a reduction of almost 40% of the route
* This is more than initally considered in my hypotheses, but it is necessary to take into account that those route is not reallistic.
* The main conclusion is that the route I got is not the optimal due to being calculated by clusters and not as a whole route, and although it may not be a reallistic route, there is room for improvement.

## Future Work
Next step is to include riders homes to evaluate the optimized route taking into account that the riders fly home after each race. It may change considerably the new route. Also try to include other constraints like no possibility to have 2 races in the same country at a row, etc.

## Workflow
The project startet with the planification, in order to get an idea of the data needed and the further steps.
After that I got the data by scraping the official MotoGP site and cleaned it. The cleaning step was finished by aggreggating the coordinates with GeoPy library.
At this point I started the analysis part applying two ML Algorithms to get some clusters, checking the results by plotting them into maps, as the features were the coordinates for each circuit.
Once I got the clusters well defined, I apply other ML algorithm to optimize the routes inside each cluster, finishing with some manual work to append all the routes to a main one.
And finally, with the new main route defined, was time to check the numbers, get insights and make conclusions.

## Organization
A trello board was my kanban model for organization.

The repository is organized in 3 folders: 
data: where you can find the data scraped as well as the cleaned data.
notebooks: with different notebooks for each step's code.
pictures: with some maps with clusters, current route and new route.

## Links

[Repository](https://github.com/GuillemGodayol/Final-Project-Optimizing-MotoGP-Calendar)  
[Slides](https://docs.google.com/presentation/d/1HQGR6QytG_Q5vxPQ-lfEDesKXXB0CmKTKq_6KGp55BM/edit?usp=sharing)  
[Trello](https://trello.com/b/wCZ9fUFN)  

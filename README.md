# 2021Fall_finals

# Analysis - Crime Data Analysis in the states of USA over the years

## The idea behind the project

Crime analysis has become an essential tool in law enforcement to enhance public safety, identify emerging trends, allocate resources, and plan crime-prevention strategies. Understanding the crime rate and factors that majorly influence crimes has become an important aspect to curb the crimes, therefore we will be focusing on the below-mentioned analysis and hypotheses to identify the significant factors that, in our view, are reasons for crimes across the US and factors that lead to changes in crimes rates every year.

# Team Members

    1. Manasi Joshi (mansj28)
    2. Shruti Deekshitula


Hypothesis 1:


Reference from :
Crime rates by state size : Based on our data taken from https://crime-data-explorer.fr.cloud.gov/pages/downloads
Highly populated states tend to have higher crime rates throughout the state
From this reference article - https://sgp.fas.org/crs/misc/R45236.pdf we are extending on the hypothesis that rate of education has no impact on crime rates.

## Hypothesis 2:
Having the different political party at state and national level influences the number of crimes

H0: Number of crimes is higher in states having different ruling party at the state and center level as compared to if the states have same ruling party
H1: Number of crimes is higher in states having same ruling party at the state and center level

We first classified the states based on the political party in each state. We then totaled the number of crimes across the years until the next election. 
Later we plotted the crime numbers in each state totaled for years 2008 - 2011, 2012 - 2015, 2016 - 2019 (Years we had data available for).


### Below are the plots for each state wise political party vs the total number of crimes through the years

![State vs Crime 2008-2011](https://user-images.githubusercontent.com/70129583/145700958-4b55bcec-8b12-43a9-8957-5d50f6b13fb3.png)

![State vs Crime 2012-2015](https://user-images.githubusercontent.com/70129583/145700964-a1186389-778e-449f-85ac-7774d1a3e7df.png)

![State vs Crime 2016-2019](https://user-images.githubusercontent.com/70129583/145700968-801e2fbb-e513-4883-af80-1ad60949705c.png)

Looking at the above graphs, we can see that states with the same ruling party (in all three plotted graphs) have a larger number of crimes than those with distinct ruling parties at the state and federal levels. 
#### As a result, our null hypothesis H0 is rejected.


We also mapped the crimes against each race in order to acquire a better understanding. The scatter plot overlaying the bar graph in the above graphs depicts total crimes against each racial category: American Indian Or Alaska Native, Asian, Black Or African American, and White. Regardless of the central elected party (democratic/republican), the number of crimes in the White category is significantly higher than in the other categories in majority of the states.


## Hypothesis 3: Holiday season affects the number of crimes

H0: There is increase in number of crimes during holiday season (Positive lean)
H1: The number of crimes do not increase during holiday season

### Below are the plots for total number of crimes in the years 2008, 2012, 2016, 2019 across the months (holiday - 11, 12 and non-holiday)

![image](https://user-images.githubusercontent.com/70129583/145702114-8e6eb1e7-3bb9-4b7b-99d7-bb97cfa884ad.png)

Looking at the above graphs, we can see that number of crimes are not affected or there is no increase in the number of crimes during holiday season months 11 (Nov), 12(Dec) 
as compared to non-holiday season. On the other hand, we can see the crimes are higher during the months 6(Jun),7(Jul)  

#### As a result, our null hypothesis H0 is rejected.

#### To further analyze the data we referred the article from - https://www.alarms.org/holiday-crime-rankings-by-state/

In the article, crime score for each state was determined as follows - 
Crime score takes into account things like holiday arrests, a state’s population, gun ownership, and poverty, and assigns each state a holiday crime score.* The higher the score, the higher the rate of holiday crime.

We have referred the above article and tried to score our crime data for the states that have the crime data information from the official site. Based on the feilds available in our datatset, we have calculated ranks for each of the field and calculated the crime score.

Crime score - Takes into account holiday crimes, property crimes, person crimes, society crimes, total crimes ranked in ascending order. The final score is calculated by averaging the ranks of selected columns for each state .

Plot the map for the user input for years between 2008-2019 for each available state data to analyze which states in the US have higher rate of holiday crime.

Below is the example of 2012 crimes in the states of US.

<img width="679" alt="2012_Crimescore" src="https://user-images.githubusercontent.com/70129583/145702175-acc44a6f-bf94-49a7-bcf4-430dace5ff64.png">

We found that a state's safety or the number of crimes committed during the holiday season in different states cannot be determined solely by scoring the dataset's available fields. There must be other important considerations to be made. To summarize, the process and steps used in the reference paper to identify the higher risk states were a good estimate based on the available data, but they do not validate concrete conclusions for any state or year.


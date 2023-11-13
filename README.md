# Political Spectrum of News Headlines
Authors: Sunny Zhou, Max Gilli, William Walker

## Purpose 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The goal of this project was to write a machine learning model that can predict the political preferences of the author based on their headline. In the current political climate, it is confusing where news articles stand on issues and what political aisle they are on. The finished project was supposed to allow individuals to input a headline and receive a rating from -2 to +2 ( -2 being far left, 0 being center, and +2 being far right).
## Data Collection
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To collect the headlines data we will be using, archives from news websites themselves (such as “CNN Site Map”). We ended up scraping 6 sites (1 for ratings -2, 0, 1, and 2, and 2 for rating -1). Some sites that will be used to gather training data included, Fox News, Washington Post, CNN, BBC, and The New York Times. In the data folder you will find the web scraping scripts. The individual data files were too large to upload onto GitHub, but there is the possibility of uploading them onto Kaggle at some point. We used the python module Beautiful Soup and Requests to navigate and access each site's sitemap, which contained the desired infromation. <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To convert texts into something our models/algorithims can work with, we will have to vectorize the texts based on a dictionary. Instead of using the entire dictionary for the english language, it was more cost effective to create the dictionary based on what the words occur in headlines. Using term frequency–inverse document frequency, chosen headlines were vectorized by whether they contain certain dictionary words, and placed as rows of a matrix X. Meanwhile, for each row i of X there will be a yi in a matrix Y to classify the headline. An attempt was made for a function to be able to vectorize any headline to use for the model. Any new words put into this function was suppose to discarded.
## Model
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; We decide to use a Naive Bayes Model for its implementation simplicity. Each word term frequency–inverse document frequency of the testing vector class was compared to each training vector, similar to pixels in an image. Due to the sizes of all the matrices, it was difficult to test and run the model in a timely matter. The model did not perform as well as we hoped.
## Future Direction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In the future, we can think about implementing a lantent semantic learning algorithim to categorize genre and related words, to increase the similarties found per political alignment. Also, like many of the recent NLP models in the field, implementation of a bi-directional model might show improvement. Future implications of the model include being used to explore how certain words/phrases vary between political views and how political veiw points can shift over time. This is why in the raw_data csv's we have a column for the date.
## Disclamer
This work was started as a part of an undergraduate special topics mathematics course taken at the University of California, Davis. It served as a proof of concept and is admittedly incomplete.

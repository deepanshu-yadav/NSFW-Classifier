Email me at awsrohanyadav@gmail.com if you want the trained model. 

# NSFW-Classifier
An AWS Sagemaker Model developed for Nudity / NSFW Images Classification <br>


This is project done for the fullfillment of Udacity Machine Learning Engineer NanoDegree. I have build a model that classifies 
input image into five categories.
1. **Nude** 
2. **Semi Nude**
3. **Animated**
4. **Porn**
5. **Safe For Work**

# Demo 
The model is deployed on aws check it yourself by downloading this repository , then going to demo folder and running index.html.


# Contents
1. [classification_tool.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/classification_tool.ipynb)
2. [clean and prepare data.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/clean%20and%20prepare%20data.ipynb)
3. [nsfw-training_built_in_aws.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/nsfw-training_built_in_aws.ipynb)
4. [nsfw_deploy.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/nsfw_deploy.ipynb)
5. [batch_transform.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/batch_transform.ipynb)
6. [benchmark.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/benchmark.ipynb)
7. [analyze_bench.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/analyze_bench.ipynb)
8. [Metrics.ipynb](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/Metrics.ipynb)
9. [analyze_results.ipynb ](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/analyze_results.ipynb)
10. [Capstone_Project_Report.pdf](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/Capstone_Project_Report.pdf)
11. [Project_Proposal.pdf](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/Project_Proposal.pdf)
12. [results.csv](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/results.csv)
13. [results_bench.csv](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/results_bench.csv)

        
         
             
  




#  Data Collection And Organization
The following guys had collected the data 
1. [B Praneeth 's Data](https://archive.org/details/NudeNet_classifier_dataset_v1) . He did an awesome job in collection 
of data . The data is for three classes <br>
   * Nude 
   * Sexy 
   *  Safe 
   1. But the problem is I need more categories for my problem . So I made a simple [tool](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/classification_tool.ipynb) that is helpful for sub classifying the above Nude Images. You just keep all the training samples in one folder and run and run it in a jupyter notebook.
I classified a few thousands of these , but then i realized that it would take a while to gather huge data. For class **Safe For Work** i sampled randomly from his huge dataset.
   2. Further More I also made a [tool](https://github.com/deepanshu-yadav/NSFW-Classifier/blob/master/useful_scripts/useful_scripts/example.py) that takes a screenshot of the screen and saves it into a folder. It becomes handy when you want to deliberately put  difficult examples in your dataset.   

The above tools proved helpful but did not solved the problem of gathering large number of examples for training. Therefore scraping was necessary.

2. [Bazarov 's Dataset](https://github.com/EBazarov/nsfw_data_source_urls) . For collecting  set of nude images I included the the sub category in the list he provided namely: <br>
   * Female genitalia
   * Male genitalia 
   * Breasts <br>
By now I had enough examples of class **nude.** <br>


3.[ Alex's Dataset](https://github.com/alex000kim/nsfw_data_scraper/tree/master/raw_data) . For classes **animated** and **porn** i scraped the data from here.
  

4.  [Instagram Scrapper](https://github.com/rarcega/instagram-scraper) For class **Semi Nude** I used his tool to scrape few Instagram pages that regularly post arousing images of men and women.  

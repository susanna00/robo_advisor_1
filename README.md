# "Robo Advisor" Project 

This is an example of Python application that allows users to evaluate a valid stock by receiving detailed information such as latest closing price, and the most recent high and low price. To ultimately help the user making a decision, the application will display a recommendation on whether it would be appropriate or not to buy the stock based on risk preferences, and stock price data visualization. 

# Prerequisite 
+ Anaconda 3.7 +
+ Python 3.7 +
+ Pip 

# Package requirements: 
Please, find below the packages required to run this program: 
+ csv 
+ os
+ json 
+ requests 
+ dotenv
+ dateitme 
+ matplotlib 

# Credentials 
Please obtain an [AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) to run this program. 

## Installation 
Fork this [remote repository](https://github.com/susanna00/robo_advisor_1) under your own control, and "clone" or download your copy of the repository onto your local computer. 

Then navigate there from your command-line application: 

```sh 
cd ~/Desktop/robo_advisor_1
```

As previously pointed out in the prerequisite, you need to create and activate a new virtual environment, called "shopping-env":

```
conda create -n stock-env python=3.8
conda activate stock-env
```
From inside the virtual environment, install package dependencies:

```
pip install -r requirements.txt
```
>NOTE: Make sure you are running it from the repository's root directory, to ensure the command does not display an error message. 

## Setup 

In the root directory of your local repository, create a new file called ".env", and update the content of the ".env" file to specify your API Key:

    ALPHAVANTAGE_API_KEY= "API Key"

# Usage 

Run the robo advisor script from the command-line:

    python app/robo_advisor.py 

+ Input the ticker symbol of the stock you wish to evaluate 
+ Input the risk you wish to accept 
+ Choose if you wish to obtain a graphical representation of the closing prices activity

## License:

This product is licensed under the MIT License. For more details, see [LICENSE.md](LICENSE.md)
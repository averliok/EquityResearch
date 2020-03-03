# Moscow Stock Exchange stock analysis tool

Program to facilitate MOEX Stock Exchange equity research.
Using MOEX API the script fetches tickers of publicly traded stocks on the Moscow Stock Exchange (MOEX). As of this update, the program allows users to get the risk and return on multiple stocks, building a bar chart to compare the relevant information among stocks.

# Checking the necessary stocks

All publicly-traded companies, as well as their tickers, can be found on the [MOEX page](https://www.moex.com/en/marketdata/#/group=4&collection=3&boardgroup=57&data_type=current&mode=groups&sort=SHORTNAME&order=asc)

When prompted, the user will be asked to input the starting and end date to conduct research. Afterward, users will be asked to put it the ticker of a company they want to research. The process will loop until given instruction otherwise.

# Merging info into a data frame

Upon completion, the program will merge all information into a single data frame and display the information. Shortly after a bar_chart.png file will be created in the relevant folder, visually presenting the analysis.

# Using the program

Upon cloning, run the main.py according to user's OS.
When run, the program will prompt you to enter the dates between which the program will fetch relevant information for user.

![Main screen](https://raw.githubusercontent.com/averliok/EquityResearch/master/EquityResearch/images/Use_1.png)

The program only takes dd/mm/yyyy format as input. Should the user type in the dates in any other format, messagebox will pop out and user will be prompted to re-enter the information.

![Invalid format](https://raw.githubusercontent.com/averliok/EquityResearch/master/EquityResearch/images/Invalid%20dates.png)

![Invalid format](https://raw.githubusercontent.com/averliok/EquityResearch/master/EquityResearch/images/Invalid%20format.png)

The program will also prompt the user if the ticker they have entered is not publicly traded on Moscow Stock Exchange and user will be asked to re-enter the information.

![Invalid ticker](https://raw.githubusercontent.com/averliok/EquityResearch/master/EquityResearch/images/Invalid%20ticker.png)

![Invalid ticker](https://raw.githubusercontent.com/averliok/EquityResearch/master/EquityResearch/images/Invalid%20Ticker.png)

After succesfully logging in the information, the user will be prompted to either continue or quit the program. The program takes 'Y' input as yes, and anything else as no (the quit button does work too).

![Use_2](https://raw.githubusercontent.com/averliok/EquityResearch/master/EquityResearch/images/Use_2.png)

Upon quitting, the bar chart representing return and risk will be created in parent folder.

![Bar_chart](https://raw.githubusercontent.com/averliok/EquityResearch/master/EquityResearch/images/bar_chart.png)

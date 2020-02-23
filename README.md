# Moscow Stock Exchange stock analysis tool

Program to facilitate MOEX Stock Exchange equity research.
Using MOEX API the script fetches tickers of publicly traded stocks on the Moscow Stock Exchange (MOEX). As of this update, the program allows users to get the risk and return on multiple stocks, building a bar chart to compare the relevant information among stocks.

# Checking the necessary stocks

All publicly-traded companies, as well as their tickers, can be found on the [MOEX page](https://www.moex.com/en/marketdata/#/group=4&collection=3&boardgroup=57&data_type=current&mode=groups&sort=SHORTNAME&order=asc)

When prompted, the user will be asked to input the starting and end date to conduct research. Afterward, users will be asked to put it the ticker of a company they want to research. The process will loop until given instruction otherwise.

# Merging info into a data frame

Upon completion, the program will merge all information into a single data frame and display the information. Shortly after a bar_chart.png file will be created in the relevant folder, visually presenting the analysis.

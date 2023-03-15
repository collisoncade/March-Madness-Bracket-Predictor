# March-Madness-Bracket-Predictor
A script that predicts the whole March Madness bracket from ESPN's Men's Tournament Challenge.

The "march_madness_predictor.py" module includes an automation written in Python that chooses one of the two teams of each game to win in each round. This is based on ESPN's "Men's Tournament Challenge" bracket on theri official website. I have not integrated the code to the website to autoselect the outcome of each game, the winners for each game will need to be entered manually. The outcome will show the first four rounds of the bracket for each division and choose if the "Top" or "Bottom" team wins. Then Final Four round and the National Chamionship round are generated in their own seperate loops. I took the scores from the last four years' national championships and took the avergae losing score and avergae winning score. I used 77 as the possible lowest score and 92 as the highest possible score. There is no bias towards any team based on their rank, it is a 50/50 chance for every game. Feedback and interactions are welcome!

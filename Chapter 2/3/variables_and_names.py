# assigns "Toronto Blue Jays" to the variable team
team = "Toronto Blue Jays"
# assigns "July 18, 2021" to the variable current_date
current_date = "July 18, 2021"
# assigns "Vladimir Guerrero Jr." to the variable player
player = "Vladimir Guerrero Jr."
# assigns 31 to the variable home_runs_to_date
home_runs_to_date = 31
# assigns 88 to the variable games_played
games_played = 88
# assigns 162 to the variable total_season_games
total_season_games = 162
# assigns 73 to the variable home_run_record
home_run_record = 73

# assigns (162 - 88 = 74) to the variable games_remaining
games_remaining = total_season_games - games_played
# assigns (31 / 88 = 0.3522727272727273) to the variable home_runs_per_game
home_runs_per_game = home_runs_to_date / games_played
# assigns (0.3522727272727273 * 162 = 57.06818181818182) to the variable projected_home_runs
projected_home_runs = home_runs_per_game * total_season_games
# assigns (57.06818181818182 > 73 = False) to the variable can_break_record
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {home_runs_per_game} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {projected_home_runs} home runs this season.")
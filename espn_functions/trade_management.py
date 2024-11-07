from data_sources.sleeper import get_sleeper_rankings

def evaluate_trade(player_out, player_in):
    sleeper_rankings = get_sleeper_rankings()
    # Calculate value difference using fantasy points from Sleeper data
    return sleeper_rankings.get(player_in.name, {}).get('fantasy_points', 0) - sleeper_rankings.get(player_out.name, {}).get('fantasy_points', 0)

def propose_trades_with_all_teams(league):
    """
    Proposes trades with every team in the league for better players.
    """
    sleeper_rankings = get_sleeper_rankings()
    
    for my_team in league.teams:
        if my_team.team_name == "Your Team Name":  # Replace with your team name
            for other_team in league.teams:
                if other_team != my_team:
                    # Go through each player in your team to find a trade candidate
                    for player_out in my_team.roster:
                        for player_in in other_team.roster:
                            trade_value = evaluate_trade(player_out, player_in)
                            if trade_value > 0:
                                league.propose_trade(player_out, player_in)
                                print(f"Proposed trade: {player_out.name} for {player_in.name}")

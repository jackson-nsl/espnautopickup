from data_sources.sleeper import get_sleeper_rankings

def get_lowest_performing_player(league, position):
    lowest_player = None
    lowest_points = float('inf')

    for team in league.teams:
        if team.team_name == "Your Team Name":  # Replace with your actual team name
            for player in team.roster:
                if player.position == position and player.total_points < lowest_points:
                    lowest_points = player.total_points
                    lowest_player = player

    return lowest_player

def pick_up_best_free_agents(league, position):
    """
    Aggressively picks up the best free agents for a position until no improvement can be made.
    """
    sleeper_rankings = get_sleeper_rankings()
    while True:
        lowest_player = get_lowest_performing_player(league, position)
        best_free_agent = None
        highest_score = 0

        for free_agent in league.free_agents(position=position):
            projected_points = sleeper_rankings.get(free_agent.name, {}).get('fantasy_points', free_agent.projected_points)
            if projected_points > highest_score:
                highest_score = projected_points
                best_free_agent = free_agent

        if best_free_agent and lowest_player and best_free_agent.projected_points > lowest_player.projected_points:
            league.drop_player(lowest_player)
            print(f"Dropped {lowest_player.name}")
            league.pickup_player(best_free_agent)
            print(f"Picked up {best_free_agent.name}")
        else:
            print(f"No worthwhile pickups left for position {position}.")
            break

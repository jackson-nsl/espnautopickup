from espn_functions.api_setup import initialize_league
from espn_functions.team_management import pick_up_best_free_agents
from espn_functions.trade_management import propose_trades_with_all_teams

def main():
    league = initialize_league()
    
    # Aggressively manage pickups for all positions
    positions = ['QB', 'RB', 'WR', 'TE', 'K', 'DST']  # Add any other positions as needed
    for position in positions:
        pick_up_best_free_agents(league, position)

    # Propose trades with all teams
    propose_trades_with_all_teams(league)

if __name__ == "__main__":
    main()

import requests

def get_sleeper_rankings():
    """
    Retrieves player data from Sleeper API and structures it by player full names.
    """
    url = "https://api.sleeper.app/v1/players/nfl"  # Sleeper players endpoint

    try:
        response = requests.get(url)
        if response.status_code == 200:
            players = response.json()
            # Structure data by full names, with checks
            return {data['full_name']: data for data in players.values() if 'full_name' in data}
        else:
            print("Failed to retrieve Sleeper data")
            return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

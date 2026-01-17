from mcp.server.fastmcp import FastMCP
from chess.chess_api import get_player_profile, get_player_stats

mcp = FastMCP("Chess.com")

@mcp.tool()
def get_chess_player_profile(username: str) -> dict:
    """Fetches the chess.com player profile for the given username."""
    return get_player_profile(username)

@mcp.tool()
def get_chess_player_stats(username: str) -> dict:
    """Fetches the chess.com player stats for the given username."""
    return get_player_stats(username)

def main():
    mcp.run()

if __name__ == "__main__":
    main()
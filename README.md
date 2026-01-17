
# MCP Chess Server Installation

## Setup Instructions

Add the following configuration to your MCP config file:

```json
{
    "mcpServers": {
        "chess_server": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/AshGhimire/mcp-chess-server.git",
                "chess"
            ],
            "type": "stdio"
        }
    }
}
```

This configuration enables the Chess Server MCP with UV package manager for dependency handling.

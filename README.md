*** MCP Server for getting stock prices and historical data ***

** To Setup ** 

- Download Claude for Desktop
- In Mac , open `~/Library/Application\ Support/Claude/claude_desktop_config.json`
- Add this `  "mcpServers": {
    "stocks": {
      "command": "/Users/[your_user_name]/.local/bin/uv",
      "args": [
        "--directory",
        "/Users/armaan/Desktop/mcp/finance-stocks",
        "run",
        "stocks.py"
      ]
    }
  }
  `
- Run `uv run stocks.py`
- Open Claude Code
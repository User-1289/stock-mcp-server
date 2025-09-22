# MCP Server for Getting Stock Prices and Historical Data

## Setup Instructions

1. **Download Claude for Desktop**

2. **Edit Config File (Mac)**
   - Open:
     ```bash
     ~/Library/Application\ Support/Claude/claude_desktop_config.json
     ```
   - Add the following block:
     ```json
     "mcpServers": {
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
     ```

3. **Run the Server**
   ```bash
   uv run stocks.py

4. **Open Claude Code**
    - Enable if not enabled in the connections
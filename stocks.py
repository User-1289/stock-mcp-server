from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import yfinance as yf
mcp = FastMCP("stocks")

@mcp.tool()
async def get_stock_price(symbol: str) -> Any:
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")["Close"].iloc[0]

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
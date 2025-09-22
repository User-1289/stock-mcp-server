from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import yfinance as yf
mcp = FastMCP("stocks")

@mcp.tool()
async def get_stock_price(symbol: str) -> Any:
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")["Close"].iloc[0]

@mcp.tool()
async def get_historical_data(symbol: str, period: str = "1mo") -> Any:
    stock = yf.Ticker(symbol)
    return stock.history(period=period).to_dict()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
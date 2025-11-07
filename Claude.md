# saxo_openapi - Saxo Bank OpenAPI Python Wrapper

## Project Overview

`saxo_openapi` is a comprehensive Python wrapper for the Saxo Bank OpenAPI REST interface. It provides a clean, Pythonic interface to interact with Saxo Bank's trading platform, enabling developers to build trading applications, access market data, manage portfolios, and execute trades programmatically.

**Version:** 0.6.0
**Author:** Feite Brekeveld
**License:** MIT
**Python Support:** Python 3.4+

## Key Features

- **Comprehensive Coverage**: Covers most Saxo Bank OpenAPI endpoints across multiple service categories
- **Request-Response Pattern**: Consistent, class-based design for all API endpoints
- **Environment Support**: Supports both simulation and live trading environments
- **Streaming Support**: Built-in support for WebSocket streaming data
- **Order Helpers**: High-level abstractions for common order types (Market, Limit, Stop orders)
- **Session Management**: Utilities for managing sessions and account information
- **Type Safety**: Defined constants and enums for order types, asset types, and other parameters

## Architecture

### Core Components

#### 1. API Client (`saxo_openapi/saxo_openapi.py`)
The central `API` class handles:
- Authentication via access tokens (Bearer token)
- Request/response lifecycle management
- Environment configuration (simulation vs. live)
- Session management with `requests.Session`
- Error handling with custom `OpenAPIError` exceptions
- Support for both regular and streaming endpoints

**Key Methods:**
- `request(endpoint)`: Execute an API request for a given endpoint
- `__request()`: Internal method for making HTTP requests
- `__stream_request()`: Internal method for streaming responses

**Environments:**
- **Simulation**: `https://gateway.saxobank.com/sim/` (prefix: sim)
- **Live**: `https://gateway.saxobank.com/` (no prefix)

#### 2. Request Classes (`saxo_openapi/endpoints/`)
All endpoints are represented by request classes that inherit from `APIRequest`:

```python
class APIRequest(metaclass=ABCMeta):
    def __init__(self, endpoint, expected_status, method="GET"):
        # Handles endpoint URL, HTTP method, status validation
```

**Endpoint Categories:**
- `accounthistory/`: Account performance, values, historical positions
- `chart/`: Chart data and price history
- `eventnotificationservices/`: Client activity notifications
- `portfolio/`: Accounts, positions, orders, balances, exposure
- `referencedata/`: Instruments, exchanges, currencies, countries, timezones
- `rootservices/`: Diagnostics, features, sessions, user info
- `trading/`: Order placement, prices, allocation keys, option chains
- `valueadd/`: Price alerts and notifications

**Design Pattern:**
Each endpoint class follows a consistent pattern:
- **Route parameters**: Required named parameters
- **Query parameters**: Optional/required `params` dict
- **Body parameters**: Optional/required `data` dict

Example:
```python
# Route parameter: PositionId is required
# Query parameters: params dict is required
r = portfolio.positions.SinglePosition(PositionId="12345", params={...})
```

#### 3. Contrib Utilities (`saxo_openapi/contrib/`)
Helper modules that simplify common tasks:

**Orders (`contrib/orders/`):**
- `baseorder.py`: Base class for order builders
- `marketorder.py`: Market order builders (MarketOrder, MarketOrderFxSpot, MarketOrderStock)
- `limitorder.py`: Limit order builders
- `stoporder.py`: Stop order builders
- `onfill.py`: Take profit and stop loss specifications
- `helper.py`: Utility functions (e.g., `direction_from_amount()`)
- `mixin.py`: Order mixins for additional functionality

**Session (`contrib/session.py`):**
- Account information retrieval
- Session management utilities

**WebSocket (`contrib/ws/`):**
- `stream.py`: WebSocket streaming client for real-time data

**Utilities (`contrib/util/`):**
- `instrument_to_uic.py`: Convert instrument identifiers to UICs

#### 4. Definitions (`saxo_openapi/definitions/`)
Constants and enums for API parameters:
- `orders.py`: Order types, duration types, asset types, amount types
- `accounthistory.py`: Account history-related definitions
- `activities.py`: Activity types for event notifications
- `reportformats.py`: Report format definitions

Example usage:
```python
import saxo_openapi.definitions.orders as OD

order_data = {
    "OrderType": OD.OrderType.Market,
    "AssetType": OD.AssetType.FxSpot,
    "AmountType": OD.AmountType.Quantity,
    "BuySell": OD.BuySell.Buy
}
```

### Directory Structure

```
saxo_openapi/
├── __init__.py              # Package initialization, API and OpenAPIError exports
├── saxo_openapi.py          # Core API client class
├── exceptions.py            # Custom exception classes
├── contrib/                 # Helper utilities and abstractions
│   ├── orders/             # Order builders (Market, Limit, Stop)
│   ├── session.py          # Session and account management
│   ├── ws/                 # WebSocket streaming support
│   └── util/               # Utility functions
├── definitions/             # Constants and enums
│   ├── orders.py           # Order-related definitions
│   ├── accounthistory.py   # Account history definitions
│   ├── activities.py       # Activity type definitions
│   └── reportformats.py    # Report format definitions
└── endpoints/               # API endpoint classes
    ├── apirequest.py       # Base APIRequest class
    ├── decorators.py       # Endpoint decorators
    ├── accounthistory/     # Account history endpoints
    ├── chart/              # Chart data endpoints
    ├── eventnotificationservices/  # Event notification endpoints
    ├── portfolio/          # Portfolio management endpoints
    ├── referencedata/      # Reference data endpoints
    ├── rootservices/       # Root services (diagnostics, sessions)
    ├── trading/            # Trading endpoints (orders, prices)
    └── valueadd/           # Value-add services (price alerts)
```

## Usage Patterns

### 1. Basic API Request

```python
from saxo_openapi import API
import saxo_openapi.endpoints.rootservices as rs

# Initialize client with access token
token = "your_access_token_here"
client = API(access_token=token)

# Make a request
r = rs.diagnostics.Get()
response = client.request(r)
print(r.status_code)  # Check status code
```

### 2. Portfolio Management

```python
import saxo_openapi.endpoints.portfolio as pf

# Get positions for logged-in client
r = pf.positions.PositionsMe()
positions = client.request(r)

# Get a specific position
r = pf.positions.SinglePosition(
    PositionId="212561926",
    params={"FieldGroups": ["PositionBase", "PositionView"]}
)
position = client.request(r)
```

### 3. Trading - Manual Order Creation

```python
import saxo_openapi.endpoints.trading as tr

# Market order body
order_body = {
    "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
    "Amount": "100000",
    "AssetType": "FxSpot",
    "BuySell": "Sell",
    "OrderType": "Market",
    "Uic": 21,  # EURUSD
    "ManualOrder": False
}

# Place order
r = tr.orders.Order(data=order_body)
result = client.request(r)
print(result["OrderId"])
```

### 4. Trading - Using Order Helpers

```python
from saxo_openapi.contrib.orders import (
    MarketOrderFxSpot,
    tie_account_to_order
)
from saxo_openapi.contrib.session import account_info

# Get account information
ai = account_info(client)

# Create market order (positive = buy, negative = sell)
order = MarketOrderFxSpot(Uic=21, Amount=100000)

# Tie to account
order_data = tie_account_to_order(ai.AccountKey, order)

# Place order
r = tr.orders.Order(data=order_data.data)
result = client.request(r)
```

### 5. Reference Data

```python
import saxo_openapi.endpoints.referencedata as rd

# Get instrument details
r = rd.instruments.InstrumentDetails(
    Uic=21,
    AssetType="FxSpot",
    params={}
)
instrument = client.request(r)

# Get all exchanges
r = rd.exchanges.ExchangeList()
exchanges = client.request(r)
```

### 6. Streaming Data

```python
# Streaming endpoints return generators
import saxo_openapi.endpoints.trading as tr

r = tr.prices.CreatePriceSubscription(data={
    "Arguments": {
        "Uic": 21,
        "AssetType": "FxSpot"
    }
})

# Stream returns a generator
for price_update in client.request(r):
    print(price_update)
```

## Endpoint Coverage

### Fully Covered ([x])
- **Account History**: Account values, historical positions, performance
- **Chart**: Charts endpoint
- **Event Notification Services**: Client activities, subscriptions
- **Portfolio**: All endpoints (accounts, positions, orders, balances, exposure, etc.)
- **Reference Data**: Most endpoints (instruments, exchanges, currencies, countries, etc.)
- **Root Services**: Diagnostics, features, sessions, user, subscriptions
- **Trading**: Orders (v2), prices, positions, allocation keys, info prices, messages, option chains
- **Value Add**: Price alerts

### Partially Covered ([.]) or Not Covered ([ ])
- **Auto Trading**: Not covered
- **Client Management**: Not covered
- **Client Reporting**: Not covered
- **Client Services**: Not covered
- **Partner Integration**: Not covered
- **Platform**: Not covered

See README.rst for complete endpoint coverage checklist.

## Configuration

### Environment Setup

```python
# Simulation environment (default)
client = API(access_token=token, environment='simulation')

# Live environment
client = API(access_token=token, environment='live')
```

### Custom Headers

```python
headers = {
    "Custom-Header": "value"
}
client = API(access_token=token, headers=headers)
```

### Request Parameters

```python
# Add timeout to all requests
client = API(access_token=token, request_params={"timeout": 5.0})
```

## Testing

The project includes comprehensive unit tests:

```
tests/
├── test_saxo_openapi.py          # Core API tests
├── test_contrib_orders.py        # Order helper tests
├── test_portfolio_*.py           # Portfolio endpoint tests
├── test_trading_*.py             # Trading endpoint tests
├── test_refdata.py               # Reference data tests
├── test_rootservices_*.py        # Root services tests
└── unittestsetup.py              # Test utilities
```

Run tests with:
```bash
pytest tests/
```

## Documentation

The project uses Sphinx for documentation:

```bash
cd docs/
make html
```

Documentation is also available at: https://saxo-openapi.readthedocs.io/en/latest

## Key Classes and Methods

### API Class
```python
API(access_token, environment='simulation', headers=None, request_params=None)
```
- `request(endpoint)`: Execute an API request

### APIRequest Class
```python
APIRequest(endpoint, expected_status, method="GET")
```
Properties:
- `status_code`: HTTP status code of the response
- `response`: Parsed response data
- `expected_status`: Expected HTTP status code

### Order Builders

**MarketOrder:**
```python
MarketOrder(Uic, Amount, AssetType, ManualOrder=False,
            AmountType=OD.AmountType.Quantity,
            TakeProfitOnFill=None, StopLossOnFill=None,
            TrailingStopLossOnFill=None)
```

**MarketOrderFxSpot:**
```python
MarketOrderFxSpot(Uic, Amount, ManualOrder=False,
                  AmountType=OD.AmountType.Quantity, ...)
```

**LimitOrder:**
```python
LimitOrder(Uic, Amount, AssetType, OrderPrice, ManualOrder=False, ...)
```

**StopOrder:**
```python
StopOrder(Uic, Amount, AssetType, OrderPrice, ManualOrder=False, ...)
```

## Error Handling

The library raises `OpenAPIError` for HTTP errors:

```python
from saxo_openapi import OpenAPIError

try:
    response = client.request(r)
except OpenAPIError as e:
    print(f"Error {e.status_code}: {e.reason}")
    print(e.message)
```

## Dependencies

Core dependencies (from requirements.txt):
- `requests`: HTTP client for API requests
- Additional dependencies managed via requirements.txt and setup.py

Development dependencies (requirements_dev.txt):
- Testing and development tools

## Important Notes

### ManualOrder Attribute
As of v0.6.0, the `ManualOrder` attribute is **required** for all order placements. This flag identifies whether an order originates from an automated system (False) or manual entry (True).

### Authentication
The library uses Bearer token authentication. Tokens can be obtained from the Saxo Developer Portal:
- https://www.developer.saxo/openapi/learn

For testing, create a 24-hour token from the developer portal.

### Rate Limiting
Be aware of Saxo Bank's rate limits. The library does not implement automatic rate limiting.

### WebSocket Streaming
Streaming endpoints use a different URL pattern and return generators for continuous data.

## Development Workflow

### Adding New Endpoints

1. Create endpoint class in appropriate `endpoints/` subdirectory
2. Inherit from the appropriate base class
3. Use the `@endpoint` decorator to define the URL pattern
4. Add response schema in `responses/` subdirectory
5. Document with examples using `@dyndoc_insert` decorator
6. Add unit tests in `tests/`

Example:
```python
from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio

@endpoint("openapi/port/v1/positions/{PositionId}")
class SinglePosition(Portfolio):
    @dyndoc_insert(responses)
    def __init__(self, PositionId, params):
        super(SinglePosition, self).__init__(PositionId=PositionId)
        self.params = params
```

### Version Management

The project uses `bumpversion` for version management:
```bash
bumpversion patch  # 0.6.0 -> 0.6.1
bumpversion minor  # 0.6.0 -> 0.7.0
bumpversion major  # 0.6.0 -> 1.0.0
```

## Jupyter Notebooks

The `jupyter/` directory contains interactive notebooks for experimentation:
- Example authentication setup
- Interactive API exploration
- Testing and prototyping

## Related Resources

- **Saxo OpenAPI Documentation**: https://www.developer.saxo/openapi/referencedocs
- **Developer Portal**: https://www.developer.saxo/
- **Package Documentation**: https://saxo-openapi.readthedocs.io/en/latest
- **GitHub Repository**: https://github.com/hootnot/saxo_openapi
- **PyPI Package**: https://pypi.org/project/saxo-openapi

## Contributing

When contributing:
1. Follow the existing code structure and patterns
2. Add tests for new functionality
3. Update documentation
4. Follow flake8 style guidelines
5. Update CHANGELOG.rst

## License

MIT License - see LICENSE file for details.

## Quick Start Example

```python
from saxo_openapi import API
import saxo_openapi.endpoints.portfolio as pf
import saxo_openapi.endpoints.trading as tr
from saxo_openapi.contrib.orders import MarketOrderFxSpot, tie_account_to_order
from saxo_openapi.contrib.session import account_info
import json

# Initialize
token = "your_24h_token_from_developer_portal"
client = API(access_token=token, environment='simulation')

# Get account info
ai = account_info(client)
print(f"Account Key: {ai.AccountKey}")

# Check current positions
r = pf.positions.PositionsMe()
positions = client.request(r)
print(f"Current positions: {positions['__count']}")

# Create and place a market order
order = MarketOrderFxSpot(Uic=21, Amount=10000)  # Buy 10k EURUSD
order_data = tie_account_to_order(ai.AccountKey, order)
r = tr.orders.Order(data=order_data.data)
result = client.request(r)
print(f"Order placed: {result['OrderId']}")

# Check positions again
r = pf.positions.PositionsMe()
positions = client.request(r)
print(json.dumps(positions, indent=2))
```

## Summary

`saxo_openapi` is a well-structured, comprehensive Python wrapper for Saxo Bank's trading API. It provides:
- Clean, consistent interface across all endpoints
- Both low-level and high-level abstractions
- Strong type definitions and constants
- Good test coverage and documentation
- Support for both simulation and live trading
- WebSocket streaming capabilities

The library is ideal for building trading bots, portfolio management tools, market data applications, and integration with Saxo Bank's trading platform.

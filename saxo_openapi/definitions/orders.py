# -*- coding: utf-8 -*-

"""Order related definitions."""

definitions = {
    'AmountType': {
        'CashAmount': 'Order amount is specified as a monetary value',
        'Quantity': 'Order Amount is specified as an amount of '
                    'lots/shares/contracts'
    },
    'AssetType': {
        'Bond': 'Bond',
        'CfdIndexOption': 'Cfd Index Option',
        'CfdOnFutures': 'Cfd on Futures',
        'CfdOnIndex': 'Cfd on Stock Index',
        'CfdOnStock': 'Cfd on Stock',
        'ContractFutures': 'Contract Futures',
        'FuturesOption': 'Futures Option',
        'FuturesStrategy': 'Futures Strategy',
        'FxBinaryOption': 'Forex Binary Option',
        'FxForwards': 'Forex Forward',
        'FxKnockInOption': 'Forex Knock In Option',
        'FxKnockOutOption': 'Forex Knock Out Option',
        'FxNoTouchOption': 'Forex No Touch Option',
        'FxOneTouchOption': 'Forex One Touch Option',
        'FxSpot': 'Forex Spot',
        'FxVanillaOption': 'Forex Vanilla Option',
        'ManagedFund': 'Obsolete: Managed Fund',
        'MutualFund': 'Mutual Fund',
        'Stock': 'Stock',
        'StockIndex': 'Stock Index',
        'StockIndexOption': 'Stock Index Option',
        'StockOption': 'Stock Option',
    },
    'Direction': {
         'Buy': 'Buy',
         'Sell': 'Sell'
    },
    'OrderDurationType': {
        'AtTheClose': 'At the close of the trading session',
        'AtTheOpening': 'At the Opening of the trading session',
        'DayOrder': 'Day order - Valid for the trading session',
        'FillOrKill': 'Fill or Kill order',
        'GoodForPeriod': 'Good for Period',
        'GoodTillCancel': 'Good til Cancel',
        'GoodTillDate': 'Good til Date',
        'ImmediateOrCancel': 'Immediate or Cancel'
    },
    'OrderType': {
        'Algorithmic': 'Algo order',
        'Limit': 'Limit Order',
        'Market': 'Market Order',
        'Stop': 'Stop Order',
        'StopIfTraded': 'Stop if traded',
        'StopLimit': 'Stop Limit Order',
        'Switch': 'Switch order, Sell X and Buy Y with one order',
        'TrailingStop': 'Trailing stop',
        'TrailingStopIfBid': 'Trailing stop if bid',
        'TrailingStopIfOffered': 'Trailing stop if offered',
        'TrailingStopIfTraded': 'Trailing stop if traded',
        'Traspaso': 'Traspaso. Specific type of switch order. Only '
                    'available on select MutualFunds',
        'TraspasoIn': 'TraspasoIn. Specific type of switch order'
    },
    'ToOpenClose': {
        'ToClose': 'Order/Position is ToClose',
        'ToOpen': 'Order/Position is ToOpen',
        'Undefined': 'Undefined'
    }
}

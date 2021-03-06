# Development Update (June 1, 2018)

[![Build Status](https://travis-ci.org/michaelchu/optopsy.svg?branch=master)](https://travis-ci.org/michaelchu/optopsy)

This library is currently being redeveloped to be better optimized for options backtesting. 

The new version will provide predefined filters to act as building blocks for your option trading strategies.
No need to extend classes to implement custom trade configurations such as position sizing and commissions. These
settings can now be defined using existing filters.

Filters will include (but not limited to):

**Entry rules:**
* Days to expiration
* Entry Days (Stagger trades)
* Absolute Delta
* Percentage out-of-the-money
* Contract size

**Exit rules:**
* Days to expiration
* Hold days
* Profit/Stop loss percent
* Spread delta
* Spread price

Development changes will be made on the `development` branch. The backtester branch will be retained for historical
purposes and will be removed at a later time.

# Optopsy

Optopsy is a flexible backtesting framework used to test complex options trading strategies written in Python. 
Backtesting is the process of testing a strategy over a given data set. This framework allows you to easily create 
strategies that mix and match different filters to create an 'Algo', these 'Algos" can in turn be combined to model various
trading techniques such as hedging or pairs trading. 
The modular nature of this framework aims to foster the creation of easily testable, re-usable and flexible blocks of strategy logic to facilitate 
the rapid development of complex options trading strategies.

## Features
* **Open source** - Feel free to make requests or contribute to the code base! Help out a fellow trader!
* **BYOD** - "Bring your own Data" source by using the built-in data adapters or write your own. (Currently supports csv files)
* **Modular Design** - Facilitates the construction and composition of complex algorithmic trading strategies that are modular and re-usable.
* **Optimization support** - Define ranges for your strategy parameters and the system will optimize the strategy

### Planned Features
* Option strategy support:
    * Single Calls/Puts
    * Vertical Spreads
    * Iron Condors (Iron Butterflies)
    * Covered Stock
    * Combos (Synthetics/Collars)
    * Diagonal Spreads
    * Calendar Spreads
    * Custom Spreads
    * Strangles
    * Straddles
 * Stock Price Distribution Generator - Analyze historical stock price movements patterns to discover potential trade ideas.
 * Trade Scanner - Used to recommend trades based on stock price distributions

### Usage

Coming Soon.

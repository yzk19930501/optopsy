from datetime import date

import pandas as pd

# import the backtest library
import optopsy as op

pd.options.display.width = None

struct = (
    ('symbol', 0),
    ('quote_date', 1),
    ('root', 2),
    ('expiration', 3),
    ('strike', 4),
    ('option_type', 5),
    ('volume', 10),
    ('bid', 12),
    ('ask', 14),
    ('underlying_price', 17),
    ('iv', 18),
    ('delta', 19),
    ('gamma', 20),
    ('theta', 21),
    ('vega', 22),
    ('rho', 23),
    ('oi', 24)
)


def run_strat():
    # fetch the pre-formatted option spread data generated by option
    data = op.get('../data/A.csv',
                  start=date(2016, 1, 1),  # using a date function here to avoid entering the wrong date format
                  end=date(2016, 12, 31),
                  struct=struct
                  )


# strategy_1 = op.Strategy('Weekly Bull Put Spread', [
#     op.algos.EntryAbsDelta(ideal=0.5, min=0.4, max=0.6),
#     op.algos.EntrySpreadPrice(ideal=1.0),
#     op.algos.EntryDaysToExpiration(ideal=47, min=40, max=52),
#     op.algos.EntryDayOfWeek(ideal=4)
# ], op.options.LongPutSpread(data, width=2))
#
# # Here we create another 'Strategy', one that is designed to hedge the strategy above
# strategy_2 = op.Strategy('Weekly Bull Put Spread Strategy', [
#     op.algos.EntryAbsDelta(ideal=0.2, min=0.4, max=0.6),
#     op.algos.EntryDaysToExpiration(ideal=47, min=40, max=52),
#     op.algos.EntryDayOfWeek(ideal=4)
# ], op.options.LongPut(data))
#
#

#     # Create an instance of Optopsy with strategy settings
#     optopsy = op.Optopsy([strategy_1, strategy_2])
#
#     # Set our desired cash start
#     optopsy.set_cash(100000)
#
#     # Print out the starting conditions
#     print('Starting Portfolio Value: %.2f' % optopsy.get_value())
#
#     # Run over everything
#     optopsy.run()
#
#     # Print out the final result
#     print('Final Portfolio Value: %.2f' % optopsy.get_value())


if __name__ == '__main__':
    run_strat()

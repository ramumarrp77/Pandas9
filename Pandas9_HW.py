# Problem 1 : Game Play Analysis I

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('player_id')['event_date'].min().reset_index()
    return activity.rename(columns= {'event_date' : 'first_login'})


# Problem 2 : Customers Placing the Largest Number of Orders


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number')['order_number'].count().reset_index()
    df=df[ df['order_number'] == df['order_number'].max() ]
    return df['customer_number'].to_frame()

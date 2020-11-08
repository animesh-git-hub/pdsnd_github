import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=''
    while city not in ('chicago','new york city','washington'):
        city= input ("please enter city name as chicago or new york city or washington:\n")
        city=city.lower()

    # get user input for month (all, january, february, ... , june)
    month=''
    while month not in ('jan','feb','mar','apr','may','jun','all'):
        month= input ("please eneter month as jan feb mar apr may jun or all:\n")
        month=month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=''
    while day not in ('m','t','w','th','f','sa','s','all'):
        day= input ("please enter day of week as m t w th f sa s or all:\n")
        day=day.lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

        # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

        days = ['m','t','w','th','f','sa','s']
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

def input_function(df):
    counter=0
    while True:
        view_data=input('\nwould you like to view raw data?Enter yes or no\n')
        if view_data.lower() =='yes':
         print (df.iloc[counter:counter+5])
        else:
         break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    # display the most common day of week
    df['day'] = df['Start Time'].dt.weekday
    popular_day = df['day'].mode()[0]

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print ('Most Popular month:',popular_month)
    print ('Most Popular day:',popular_day)
    print ('Most Popular Start Hour:',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_st=df['Start Station'].mode()[0]

    print ('Most Popular Start Station:',popular_start_st)
    # display most commonly used end station
    popular_end_st=df['End Station'].mode()[0]
    print ('Most Popular End Station:',popular_end_st)

    # display most frequent combination of start station and end station trip
    df['Start&End']=df['Start Station']+' AND '+df['End Station']
    popular_start_end_st=df['Start&End'].mode()[0]
    print ('Most Popular combinaton of Start station and End Station:',popular_start_end_st)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time (ttt)
    ttt=df['Trip Duration'].sum()
    print ('total travel time:',ttt)

    # display mean travel time (mtt)
    mtt=df['Trip Duration'].mean()
    print ('total mean travel time:',mtt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print ('Count of user types\n')
    print (user_types)

# Display counts of gender

    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print ('\nCount of gender\n')
        print (gender)

# Display earliest, most recent, and most common year of birth(yob)
    if 'Birth Year' in df:
        earliest_yob=int(df['Birth Year'].min())
        print ('\nearliest year of birth:',earliest_yob)

        recent_yob=int(df['Birth Year'].max())
        print ('most recent year of birth:',recent_yob)

        common_yob=int(df['Birth Year'].mode()[0])
        print ('most common year of birth:',common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        input_function(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()


Making first change

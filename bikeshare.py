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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("\nWhich city does user want to explore? chicago, new york city or washington?\n").lower()
        if city not in cities:
            print("select a new city")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    
    while True:
        month = input("\nChoose a preferred month from january, february, march, april, may, june or select 'all' if you have no choice\n").lower()
        if month not in months:
            print("you can select 'all' from this list")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    while True:
        day = input("\n please select from the list of days monday, tuesday, wednesday, thursday, friday, \n saturday, sunday or select 'all' for none\n").lower()
        if day not in days:
            print("you can simply selct the choice 'all' to continue")
            continue
        else:
            break


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
    # load data for city
    df = pd.read_csv(CITY_DATA[city])
    
    # start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day and hour selected by the user
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    #filter by day 
    
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) + 1
        df = df[df['day'] == day]
        


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)


    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('Most common day:', most_common_day)


    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station:', most_common_start_station)
                                                                         

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('Most common end station:', most_common_end_station)
    

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df.groupby(['Start Station', 'End Station']).count()
    print('Most common start and end stations:', most_common_start_station, most_common_end_station)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel time:', total_travel_time)


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:', user_types)
    
    # TO DO: Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print('Gender type:', gender_type)
    except KeyError:
        print('Gender type not applicable')


                   
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = int(df['Birth Year'].min())
    print('Earliest Year:', earliest_year)
    
    most_recent_year = int(df['Birth Year'].max())
    print('Most recent year:', most_recent_year)
    
    most_common_birth_year = int(df['Birth Year'].value_counts().idxmax())
    print('Most Common Birth Year:', most_common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays the rows of data upon request by user.
    
    shows 5 lines of code upon each entry""" 
    
    print('press enter to see the next 5 rows, no to skip')
    
    start_loc = 0
    while (input() != 'no'):
        start_loc += 5
        print(df.head(start_loc))
    

              
def main():
              while True:
                city, month, day = get_filters()
                df = load_data(city, month, day)
              
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
                display_data(df)
                
              
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break
if __name__ == "__main__":
	main()

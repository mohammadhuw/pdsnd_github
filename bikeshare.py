import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = { 'january':1, 'february':2,'march':3,'april':4,'may':5,'june':6, 'all':'all'}
days = [ 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

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
    city = input('please enter cities chicago, new york city, washington ').lower()
    while city not in CITY_DATA:
            print('you enter the wrong city, please try again ')
            city = input('please enter cities chicago, new york city, washington ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('please enter a month or chose all ').lower()
    while month not in months:
        print('you enter a wrong chose, please try again ')
        month = input('please enter a month or chose all ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('please enter a day or chose all ').lower()
    while day not in days:
        print('you enter a wrong chose, please try again ')
        day = input('please enter a day or chose all ').lower()
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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        df = df[df['month'] == months[month]]
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month is ' , df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('the most common day of week is ' , df['day'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('the most common start hour is ' , df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common start station is ' , df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('the most common end station is ' , df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['station'] = df['Start Station'] + df['End Station']
    print('The most common start and end station combo is ' , df['station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    df['travel'] = df['Trip Duration'].sum()
    print('The total travel time is ', df['travel'].mode()[0])

    # TO DO: display mean travel time
    df['travel'] = df['Trip Duration'].mean()
    print('The mean travel time is ', df['travel'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
  
   # TO DO: Display counts of user types
    df["User Type"] = df["User Type"]
    print('the counts of user type is \n', df['User Type'].value_counts()) 

    # TO DO: Display counts of gender
    
    if 'Gender' not in df.columns:
        print('this city have no gender ')
    else:
      mode = df['Gender'].value_counts()  
      print('Gender count is :',mode)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('this city have no birth year data\n')
    else:    
      mode = df['Birth Year'].value_counts()
      print('most common year of birth is \n',mode)
      print('most recent year of birth is ', df['Birth Year'].max())
      print('most earliest year of birth is ', df['Birth Year'].min())
        

    
    
   
   
    
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def display_data(df):
    start = 0
    end = 5
    start_data = input('do you want to see more data? ').lower()
    if start_data == "yes":
       while end <= df.shape[0] :

           print(df.iloc[start:end])
           start += 5
           end += 5

           end_data = input("Do you want continue? ").lower()
           if end_data == 'no':
               break
   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        print()
        if restart != 'yes' and restart != 'y' and restart != 'yus':
            break

if __name__ == "__main__":
	main()


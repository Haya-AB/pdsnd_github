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
    print ('This project use Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.')
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        #print ('Please, Capitalize each enter word')
        city1= input('Would you like to see data for Chicago, New York City, or Washington? \n')
        city = city1.lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print('Sorry, invalid value. Please enter the city name.')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month2 = input('Would you like to filter the data by month? If yes, write month name else write All \n')
      month = month2.lower()
      if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        print("Sorry, invalid value. Please enter the month name.")
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day1 = input('Would you like to filter the data by day? If yes, write day name else write All \n')
      day = day1.lower()
      if day not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
        print("Sorry, invalid value. Please enter the day name.")
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print ('The Most Common Month : ', most_common_month )

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print ('The Most Common Day : ', most_common_day )

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print ('The Most Common Start Hour : ', most_common_start_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print ('The Most Commonly Used Start Station : ', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print ('The Most Commonly Used End Station : ', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination_start_station_end_station_trip1 = (df['Start Station'] + '&' + df['End Station']).mode()[0]
    most_frequent_combination_start_station_end_station_trip = str(most_frequent_combination_start_station_end_station_trip1.split('&')) 
    print ('The Most Frequent Combination of Start Station and End Station Trip : ', most_frequent_combination_start_station_end_station_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_trav_time = df['Trip Duration'].sum()
    print ('The Total Travel Time is : ', tot_trav_time)

    # TO DO: display mean travel time
    mn_trav_time = df['Trip Duration'].mean()
    print ('The Mean Travel Time is : ', mn_trav_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    cou_user_types1 = df['User Type'].value_counts()
    cou_user_types = cou_user_types1
    print ('The Count of User Types is : ', cou_user_types)

    # TO DO: Display counts of gender
    if city == 'washington':
        print (' The gender is not available for washington city')
    elif city == 'chicago' or city == 'new york city':
        cou_gender1 = df['Gender'].value_counts()
        cou_gender = cou_gender1
        print ('The Count of Gender is : ', cou_gender)
         

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print (' The birth data is not available for washington city')
    elif city == 'chicago' or city == 'new york city':
        earliest_year_birth = df['Birth Year'].min()
        print ('The Earliest Year of Birth is ', earliest_year_birth)
        most_resent_year_birth = df['Birth Year'].max()
        print ('The Most Resent Year of Birth is ', most_resent_year_birth)
        most_common_year_birth = df['Birth Year'].mode()[0]
        print ('The Most Common Year of Birth is ', most_common_year_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    x = 0
    show_row_data = input('\nWould you like to print raw data? Enter yes or no.\n')
    if show_row_data.lower() != 'yes':
        return
    print(df.head())
    while True :
        show_row_data1 = input('\nWould you like to print next raw data? Enter yes or no.\n')
        if show_row_data1.lower() != 'yes':
            return
        x = x+5
        print(df.iloc[x:x+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

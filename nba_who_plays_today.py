import json
import requests
import sys

from datetime import date
from dateutil import parser

class NbaWhoPlaysToday():
    def __init__(self, timezone):
        self.timezone = timezone
        self.schedule_url = f'https://site.web.api.espn.com/apis/v2/scoreboard/header?sport=basketball&league=nba&region=us&lang=en&contentorigin=espn&buyWindow=1m&showAirings=buy%2Clive%2Creplay&showZipLookup=true&tz={timezone}'
        self.today = date.today().strftime('%Y-%m-%d')
        self.current_year = date.today().year

    def get_schedule_json(self):
        headers = { "Accept": "application/json"}
        response = requests.get(self.schedule_url, headers=headers)
        response.raise_for_status()
        return response.json()

    def events_today(self):
        response = self.get_schedule_json()
        events = response['sports'][0]['leagues'][0]['events']
        num_events_today = len(events)
        print(f"There are: {num_events_today} games today.")
        print("--------------------------------------------")
        for event in events:
            broadcasts = event.get('broadcasts', None)
            if broadcasts:
                for broadcast in broadcasts:
                    if broadcast['type'] == 'TV':
                        date = event['date']
                        dt_date = parser.parse(date)
                        formatted_date = dt_date.strftime('%Y-%m-%d')
                        if formatted_date==self.today:
                            print(event['summary'])
                            print(event['name'])
                            print(event['seriesSummary'])
                            print(f"Broadcasting on: {broadcast['name']}")
                            print("=================================")
            else:
                summary = event['summary']
                if '/' in summary:
                    split_summary = summary.split("/")
                    month = split_summary[0]
                    day = split_summary[1]
                    day_split = day.split("-")
                    day = day_split[0].strip()
                    self.current_year
                    parsed_date = parser.parse(f'{month}/{day}/{self.current_year}')
                    formatted_date = parsed_date.strftime('%Y-%m-%d')
                    if formatted_date==self.today:
                        print(formatted_date)
                        print(event['name'])
                        print(event['seriesSummary'])
                        print("No broadcast found.")
                        print("=================================")
                else:
                    print(summary)
                    print(event['name'])
                    print(event['seriesSummary'])
                    print("No broadcast found.")
                    print("=================================")

    def main(self):
        self.events_today()


def select_timezone(timezone):
    if timezone==str(1):
        print("You selected: Eastern")
        print("Here you go!")
        timezone = "America/New_York"
        return timezone
    elif timezone==str(2):
        print("You selected: Central")
        print("Here you go!")
        timezone = "America/Chicago"
        return timezone
    elif timezone==str(3):
        print("You selected: Mountain")
        print("Here you go!")
        timezone = "America/Denver"
        return timezone
    elif timezone==str(4):
        print("You selected: Pacific")
        print("Here you go!")
        timezone = "America/Los_Angeles"
        return timezone
    elif timezone==str(5):
        print("You selected: Alaska")
        print("Here you go!")
        timezone = "America/Juneau"
        return timezone
    elif timezone==str(6):
        print("You selected: Hawaii")
        print("Here you go!")
        timezone = "America/Honolulu"
        return timezone
    else:
        print("You did not select anything from the list.")
        print("Bye bye!")
        sys.exit(1)

if __name__ == "__main__":
    timezone = input("Select a timezone:\n1.Eastern\n2.Central\n3.Mountain\n4.Pacific\n5.Alaska\n6.Hawaii\n")
    selected_timezone = select_timezone(timezone)

    NbaWhoPlaysToday(selected_timezone).main()


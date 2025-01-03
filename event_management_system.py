
# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and a method get_participant_count 
# to retrieve the current count.


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Total participants: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

# Demonstration script
if __name__ == "__main__":
    # Create an instance of Event
    event = Event("Conference", "2025-06-15")

    # Add participants
    event.add_participant()
    event.add_participant()
    event.add_participant()

    # Retrieve and display participant count
    print(f"Total number of participants in the event '{event.name}': {event.get_participant_count()}")

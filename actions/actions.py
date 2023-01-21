# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionBookMeeting(Action):

    def name(self) -> Text:
        return "action_book_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        name = tracker.get_slot("attendee")
        print(name)
        date = tracker.get_slot("date")
        print(date)
        time = tracker.get_slot("time")
        print(time)


        # print("Booked with " +name+" on "+date+" at "+time)
        dispatcher.utter_message(text="Meeting Booked")

        return []

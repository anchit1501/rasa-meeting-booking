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
        print('Hiii')
    
        # name = tracker.get_slot("attendee")
        # date = tracker.get_slot("date")
        # time = tracker.get_slot("time")


        # print("Booked with " +name+" on "+date+" at "+time)
        dispatcher.utter_message(text="Hello World!")

        return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import List, Dict, Text, Any

from rasa_sdk import Action, Tracker


class ActionUtter(Action):
    def name(self) -> Text:
        return "action_utter_internship_plan"

    async def run(self, dispatcher, tracker: Tracker, domain) -> List[Dict[Text, Any]]:
        message = f"Here are list of pending courses: "
        json_message = {"text": message,
                        "table": {
                            "headers": [
                                {"data": "Content"},
                                {"data": "Datetime"},
                                {"data": "Actor"}
                            ],
                            "rows": [
                                [
                                    {"class": "web-link",
                                     "value": "TEACHER ASSOCIATES STUDENTS ON THE PURPOSE AND REQUIREMENTS OF PRACTICAL INTERNATIONAL INTERNATIONAL, INSTRUCTIONS STUDENTS TO FIND AGENCIES THAT CAN ACCEPT TTTT students."},
                                    {"class": "web-link", "value": "07.03.2014 – 15.03.2014"},
                                    {"class": "web-link", "value": "GVCV of courses with SVTTT"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "Students receive a letter of recommendation to contact the internship location (class staff receive it at the Faculty's Office and give it to you)."},
                                    {"class": "web-link", "value": "11.03.2014 – 13.03.2014"},
                                    {"class": "web-link", "value": "VPK"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "Receive feedback from agencies and units on student admission (students can directly submit the receipt form of the agency, where to receive: VP Faculty)."},
                                    {"class": "web-link", "value": "25.04. 2014"},
                                    {"class": "web-link", "value": "VPK"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "Management of TTTT students: - Browse internship points. - Assign students to agencies.- Prepare relevant papers for students."},
                                    {"class": "web-link", "value": "28.04.2014 – 02.05.2014"},
                                    {"class": "web-link", "value": "Bachelor of Science. Head/Deputy BM. Ministry"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "- Student meeting, disseminating regulations. Students see the official assignment list. Students receive relevant documents for internship."},
                                    {"class": "web-link", "value": "06.05. 2014"},
                                    {"class": "web-link",
                                     "value": "Bachelor of Science. Ministry. Student. Head/Deputy BM"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "Students start internship (8 weeks)"},
                                    {"class": "web-link", "value": "12.05. 2014 – 05.07. 2014"},
                                    {"class": "web-link", "value": "Students"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "Assign teachers to visit students TTTT. The teacher visits the agency to visit the interns, monitor the internship progress and grade the report. The teacher does not guide the students like the thesis guide. Students practice and follow the requirements of professional instructors at the agency."},
                                    {"class": "web-link", "value": "13.05. 2014"},
                                    {"class": "web-link", "value": "Bachelor of Science. Ministry. Subject"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "Teachers visit students to practice at agencies."},
                                    {"class": "web-link", "value": "02.06. 2014 – 14.06. 2014"},
                                    {"class": "web-link", "value": "Assigned teacher"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "Students submit the internship report to the teacher in charge."},
                                    {"class": "web-link", "value": "10.07. 2014- 11.07.2014"},
                                    {"class": "web-link", "value": "Students"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "The teacher marks the results of the TTTT and enters the scores."},
                                    {"class": "web-link", "value": "14.07.2014 – 18.07.2014"},
                                    {"class": "web-link", "value": "Teacher"},
                                ],
                                [
                                    {"class": "web-link",
                                     "value": "Do the payment procedures"},
                                    {"class": "web-link", "value": ""},
                                    {"class": "web-link", "value": "Ministry"},
                                ],
                            ]
                        }}

        dispatcher.utter_message(json_message=json_message)
        return []

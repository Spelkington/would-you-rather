import os
import pandas as pd

class Scenario:
    def __init__(
        self,
        s_dict: dict,
        window_size: int=80
    ):
        """
        An object representation of a survey scenario containing scenario text and tags
        relating to the properties of the scenario

        Args:
            s_dict (dictionary): A question dictionary formatted in the format:

                {
                    "text": "eat a Snickers?",
                    "tags": [
                        "chocolate",
                        "peanut",
                        "caramel",
                        "chewy"
                    ]
                }

            window_size (int, Optional): The size of the text output window used for
                Scenario comparisons in, character length. Defaults to 80 characters.
        """
        self.text = s_dict["text"]
        self.tags = s_dict["tags"]
        self._window_size = window_size


    def __gt__(
        self,
        other: "Scenario",
        left_input="a",
        right_input="d"
    ):
        """
        Compares one scenario to another scenario in a "Would You Rather"-style context,
        where user input is used to determine if one scenario is preferable to another.

        Args:
            other (Scenario): A scenario to be compared to this scenario
            left_input (char): Keyboard character used to determine left-side preference.
                Defaults to "h".
            right_input (char): Keyboard character used to determine right-side
                preference. Defaults to "l".

        Returns:
            (boolean) True if this scenario is preferable to the other, false if not
        
        Example:
            If this scenario regards Snickers and the other regards Gummy Bears, this
            comparator is equivalent to:

            "Would you rather eat a Snickers or eat gummy bears?"
        """
        # Print query
        Scenario._format_comparison(
            self.text,
            other.text,
            left_input,
            right_input,
        )

        # Retrieve response
        response = Scenario._await_response()

        # Clear screen
        os.system('clear')
        
        return response == left_input


    def _await_response():
        while True:
            user_input = input()
            if user_input:
                return user_input[0]


    # Static Methods
    def _format_comparison(
        left_text: str,
        right_text: str,
        left_char: str,
        right_char: str,
    ):

        l = left_char.upper()
        r = right_char.upper()
        left_margin = " " * (len(left_text) // 2)
        right_margin = " " * (len(right_text) // 2)
        text_insert = f"{left_margin}[ {l} ]{left_margin}{right_margin}[ {r} ]"
        print()
        print(f"Would you rather [ {left_text} ] or [ {right_text} ]?")
        print(f"                  {text_insert}")

    def compile_list(scenarios, path):
        sorted_dicts = []
        for i, scenario in enumerate(scenarios):
            sorted_dicts.append({
                "rank": i + 1,
                "scenario": scenario.text,
                "tags": scenario.tags
            })

        df = pd.DataFrame(sorted_dicts)
        df.to_csv(path)
class verifyComponent:
    def __init__(self, backend, frontend):
        self.backend = backend  # Backend component to retrieve correct words
        self.frontend = frontend

    def verify_word_match(self, user_input, clothing_label):
        """
        Verify if the user's input matches the correct word for the given clothing label.

        Args:
            user_input (str): The word selected by the user.
            clothing_label (str): The label of the clothing item (e.g., "shirt", "pants").

        Returns:
            dict: A dictionary containing the verification result and feedback.
        """
        try:
            # Retrieve the correct word from the backend
            correct_word = self.backend.get_correct_word(clothing_label)

            # Compare the user's input with the correct word
            if user_input == correct_word:
                return {
                    "status": "correct",
                    "message": "Your selection is correct!",
                    "correct_word": correct_word
                }
            else:
                return {
                    "status": "incorrect",
                    "message": "Your selection is incorrect.",
                    "correct_word": correct_word
                }
        except Exception as e:
            # Handle errors (e.g., backend failure)
            return {
                "status": "error",
                "message": f"An error occurred: {str(e)}"
            }
        
    def provide_feedback(self, user_input, clothing_label):
        """
        Provide feedback to the front-end based on the verification result.

        Args:
            user_input (str): The word selected by the user.
            clothing_label (str): The label of the clothing item (e.g., "shirt", "pants").
        """
        # Verify the word match
        verification_result = self.verify_word_match(user_input, clothing_label)

        # Send feedback to the front-end
        if verification_result["status"] == "correct":
            self.frontend.display_feedback(
                message=verification_result["message"],
                score_update=1  # Increment score by 1 for correct answer
            )
        elif verification_result["status"] == "incorrect":
            self.frontend.display_feedback(
                message=verification_result["message"],
                correct_word=verification_result["correct_word"],
                score_update=0  # No score update for incorrect answer
            )
        else:
            # Handle errors
            self.frontend.display_error(verification_result["message"])
from survey import AnonymousSurvey

my_survey = AnonymousSurvey('What language did you first learn to speak?')
my_survey.store_response('English')
print(my_survey.responses)

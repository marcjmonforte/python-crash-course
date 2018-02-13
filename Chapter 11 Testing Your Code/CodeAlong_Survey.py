import unittest

class AnonymousSurvey(object):
	"""Collect anonymous answers to a survey question."""

	def __init__(self, question):
		"""Store a question, and prepare to store answers."""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Show the survey question."""
		print self.question

	def store_response(self, new_response):
		"""Store a single response to the survey."""
		self.responses.append(new_response)

	def show_results(self):
		"""Show all the responses that have been given."""
		print "Survey Results:"
		for response in self.responses:
			print " * " + response

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey."""

	def setUp(self):
		"""Create a survey and a set of responses for use in 
		all test methods."""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()
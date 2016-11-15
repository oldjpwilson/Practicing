#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

form = """
<form method = "post">
			<h2>What is your birthday</h2>
			<label>
				Day: 
				<input name="day">
			</label>
			<label>
				Month: 
				<input name ="month">
			</label>
			<label>
				Year: 
				<input name ="year">
			</label>
			<input type = "submit">
		</form>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(form)

	def post(self):
		self.response.out.write("Thanks for submitting my boet!")
		self.response.out.write(form)

#This is the url mapping section, and it maps to Mainpage
app = webapp2.WSGIApplication([('/', MainPage)], debug = True)


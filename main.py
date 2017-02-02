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
import re
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }

        .big{
            line-height: 1.5
        }
    </style>
</head>
<body>
    <h1> Signup</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

def build_page(username,email,error_username,error_password,error_verify,error_email):

    username_row = '''<td><label for="username">Username</label></td>
                        <td>
                            <input name="username" type="text" value="''' + username + '''"required>
                            <span class="error">'''+ error_username +'''</span>
                        </td>'''
    password_row = '''<td><label for="password">Password</label></td>
                        <td>
                            <input name="password" type="password" required>
                            <span class="error">'''+ error_password +'''</span>
                        </td>'''
    verify_row = '''<td><label for="verify">Verify Password</label></td>
                        <td>
                            <input name="verify" type="password" required>
                            <span class="error">'''+ error_verify +'''</span>
                        </td>'''
    email_row = '''<td><label for="email">Email (optional)</label></td>
                        <td>
                            <input name="email" type="email" value=''' + email + '''>
                            <span class="error">'''+ error_email +'''</span>
                        </td>'''

    form_table = '''<form method="post">
                <table class="big">

                    <tr>
                        {0}
                    </tr>

                    <tr>
                        {1}
                    </tr>

                    <tr>
                        {2}
                    </tr>

                    <tr>
                        {3}
                    </tr>

                </table>
                <br/>
                <input type="submit">
            </form>'''.format(username_row, password_row, verify_row, email_row)



    return page_header + form_table + page_footer

username_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and username_re.match(username)

pass_re = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and pass_re.match(password)

email_re  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or email_re.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = build_page("","","","","","")

        self.response.write(content)

    def post(self):

        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""

        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        if not valid_username(username):
            error_username = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            error_password = "That wasn't a valid password."
            have_error = True

        elif password != verify:
            error_verify = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            error_email = "That's not a valid email."
            have_error = True

        if have_error:

            content = build_page(username,email,error_username,error_password,error_verify,error_email)

            self.response.write(content)
        else:
            self.redirect('/welcome?username=' + username)



class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        content = '''<h1>Welcome, ''' + cgi.escape(username, quote=True) + '''!</h1>'''

        self.response.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)

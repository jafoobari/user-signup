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

def build_page(username,email):

    username_row = '''<td><label for="username">Username</label></td>
                        <td>
                            <input name="username" type="text" value="''' + username + '''"required>
                            <span class="error"></span>
                        </td>'''
    password_row = '''<td><label for="password">Password</label></td>
                        <td>
                            <input name="password" type="password" required>
                            <span class="error"></span>
                        </td>'''
    verify_row = '''<td><label for="verify">Verify Password</label></td>
                        <td>
                            <input name="verify" type="password" required>
                            <span class="error"></span>
                        </td>'''
    email_row = '''<td><label for="email">Email (optional)</label></td>
                        <td>
                            <input name="email" type="email" value=''' + email + '''>
                            <span class="error"></span>
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


class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = build_page("","")

        self.response.write(content)


# class WelcomeHandler(webapp2.RequestHandler):



app = webapp2.WSGIApplication([
    ('/', MainHandler)
    # ('/welcome', WelcomeHandler)
], debug=True)

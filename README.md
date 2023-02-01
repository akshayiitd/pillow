Pillow Backend Exercise-1

Description
Considering a single node environment where the server is deployed, Implement an API
which when called returns the number of requests made till now and rate limits any
requests after X requests with 60 seconds. Return a 429 HTTP error response when the
user hits the rate limit X. The response header should also contain the X-WAIT-TILL
(time when the next API request to succeed) and X-RATE-LIMIT (the rate limit X
enforced) details.
Points to Consider
Limit should be made configurable in the backend.
No libraries or external SDKs should be used.
Input and output should be in JSON format.
Implementation to consider huge volume for X.
Record the rate-limited requests for future debugging. (Good to Have)
Test cases or Scripts to replicate rate limiting. (Good to Have)
Tech Stack
Python3 language with flask framework.

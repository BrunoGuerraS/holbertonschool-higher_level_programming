#!/bin/bash
#sends a POST request to the passed URL, and displays the body of the response
curl -X POST ${1} -s -d "email=test@gmail.com&subject=I will always be here for PLD"

#!/bin/bash
#displays the body of the response
curl -X GET ${1} -s -H "X-School-User-Id: 98"

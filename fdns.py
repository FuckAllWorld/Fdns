#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# author:FuckAllWorld

import gzip
import argparse
import json

def getparser():
    parser = argparse.ArgumentParser(description="*"*40)
    parser.add_argument("-d","--domain",help="example:google.com")
    parser.add_argument("-r", "--record", help="example:a.cname,mx")
    parser.add_argument("-o","--output",help="example:xxx.txt")
    parser.add_argument("-f","--file",help="input .gz file")
    args = parser.parse_args()
    domain = args.domain
    record = args.record
    file = args.file
    output = args.output
    extract(domain, record, file,output)

def  extract(domain,record,file,output):
    with gzip.open(file,"r") as f:
        if record == "mx":
            for line in f:
                if domain in line.decode("utf-8"):
                    body = json.loads(line)
                    if body["type"] =="mx":
                        print(body)
        elif record == "a":
            for line in f:
                if domain in line.decode("utf-8"):
                    body = json.loads(line)
                    if body["type"] =="a":
                        if body['name'].endswith("." + domain):
                            print(body['name']+ ":" + body['value'])
if __name__ == '__main__':
    getparser()


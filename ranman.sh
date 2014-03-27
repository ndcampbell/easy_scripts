#!/usr/bin/env bash

man $(ls /usr/share/man/man1 | shuf -n 1  | cut -d '.' -f 1)


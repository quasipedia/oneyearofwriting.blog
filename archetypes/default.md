---
title = "{{ replace .Name "-" " " | title }}"
slug = '{{ .File.ContentBaseName }}'
pubdate = '{{ time.Format "1900-12-31" $t }}'
draft = true
summary = ""
tags = []
---

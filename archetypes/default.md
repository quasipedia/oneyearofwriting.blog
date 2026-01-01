+++
title = "{{ replace .Name "-" " " | title }}"
#title = '{{ replace .File.ContentBaseName "-" " " | title }}'
slug = '{{ .File.ContentBaseName }}'
pubdate = '{{ .Date }}'
draft = true
summary = ""
tags = []
+++

{{ partial "google_analytics.html" . }}

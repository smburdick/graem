# Graem Wiki

[![GitHub version](https://badge.fury.io/gh/smburdick%2Fgraem.svg)](https://badge.fury.io/gh/smburdick%2Fgraem)
![Build Status](https://github.com/smburdick/graem/actions/workflows/jekyll.yml/badge.svg)

A wiki platform for the Graem campaign setting.

Forked from [StrikingLoo's Jekyll template](https://github.com/StrikingLoo/Personal-Wiki-Site-Setup)

## Live site

[Link](https://smburdick.github.io/graem)

## Setup

To host the site locally, run

```
sudo gem install rails
sudo gem install jekyll
sudo gem install jekyll bundler
bundle install
bundle add jekyll
bundle exec jekyll serve
```

## Creating new wiki pages

The directory structure is:
```
wiki
└── article
    ├── index.md
    └── img.jpeg
    [...]
```
Each `index.md` file has this header:
```
---
title: "Article"
date: YYYY-MM-DD
description: "Description"
tags: tag1, tag2[, ...]
---
```

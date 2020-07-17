# Automatic-summarization

> This project was undertaken to apply the concepts of Natural language processing and build a simple summariser that I can build on in my internship at Cisco. 

When we have unbelievably huge amount of data, it is impossible for a user to get insights. Furthermore, a large portion of this data is either redundant or doesn't contain much useful information. The most efficient way to get access to the most important parts of the data is to summarize the data in a way that it contains non-redundant and useful information only. The data can be in any form such as audio, video, images, and text. In this project, I have used an algorithm that is based on frequency of words

## Data 

This code takes any article as input and provides a summary for it. One such sample article i used is found here: https://projects.voanews.com/greenland/

## Run

To run, use the following command:
```
python Summarizer.py <filename> -l <length of expected summary>
```
The length field is optional and defaults to 4

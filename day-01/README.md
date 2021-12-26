# Day 1 - Which of the Following is Not an Object in Python

I posted a fun Python puzzle as a [poll on LinkedIn](https://www.linkedin.com/posts/codesolid_activity-6876639846971015168-Sd-l/) where I asked folks to guess which of several things was not an object in Python.

Today I thought it would be fun to record a video to share how I discovered the answer.  Once I knew the answer, of course, writing the poll was the easy part.

Spoiler alert, the video uses one of my favorite exploratory Python functions.

Here again is the original poll:

## Which of the following is NOT an object in Python?

* String literals
* Operators:  Winner winner, chicken dinner!
* Number literals
* Docstring comments

## Watch the video on Youtube

 
How can I embed a YouTube video on GitHub wiki pages?
Asked 9 years, 4 months ago
Active 8 days ago
Viewed 193k times

388


87
I am fairly new to markup (though it's extremely easy to pickup). I am working on a package and am trying to get the wiki pages looking nice as a help manual. I can insert a YouTube video link into the wiki page pretty easily but how do I embed a YouTube video. I know this may not be possible.

I have read you can use HTML tags so I tried embedding with HTML per this link as follows:

<object width="425" height="350">
  <param name="movie" value="http://www.youtube.com/user/wwwLoveWatercom?v=BTRN1YETpyg" />
  <param name="wmode" value="transparent" />
  <embed src="http://www.youtube.com/user/wwwLoveWatercom?v=BTRN1YETpyg"
         type="application/x-shockwave-flash"
         wmode="transparent" width="425" height="350" />
</object>
And saved the page but nothing happened.

Is it possible to embed a YouTube video on GitHub wiki pages?
If so how?
video
github
youtube
embed
markdown
Share
Improve this question
Follow
edited Jun 25 at 19:53

damon
13.5k1414 gold badges5252 silver badges7373 bronze badges
asked Aug 4 '12 at 0:12

Tyler Rinker
102k6060 gold badges301301 silver badges487487 bronze badges
3
See also stackoverflow.com/questions/4279611/… – 
Brian Burns
 Nov 17 '16 at 15:44
Add a comment
13 Answers

618

It's not possible to embed videos directly, but you can put an image which links to a YouTube video:

[![Object Exploration in Python with dir and type](https://img.youtube.com/vi/ZM7iA9p-3qs/0.jpg)](https://www.youtube.com/watch?v=ZM7iA9p-3qs)


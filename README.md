# django news

This is a fork of Django News from [cchmc-bmi-os/django-news](https://github.com/cchmc-bmi-os/django-news)
by Byron Ruth <b@devel.io> and Kevin Murphy <murphyke@email.chop.edu>
which is a fork of [monokrome/django-news](https://github.com/monokrome/django-news) by Brandon R. Stoner <monokrome@monokro.me>.

## Original description:

A Django application for posting news. This is a fairly decent *news or blogging* application, and easily provides features like comments, markup, and RSS and ATOM feeds at no cost. However it makes no assumptions regarding your design, and therefore doesn't include any WYSIWYG/WYSIWYM editors or anything like that. You can easily add your own by simply applying it to <textarea> elements with a 'text-edit' class. This application also ties into the django user authentication system to allow multiple users to post, edit, and delete news articles on the web site.

## Tweaks by:

* Marcus Renno <marcus.renno@cchmc.org>

## Release Notes

0.7.2 - Differences from the forked version:

* Fixed template lazy references
* Using Django generic views 
* Fixed detail link
* Fixed RSS v1, RSS v2 and Atom feed
* Removed unused methods 
* Formatted to be consistent over the whole project 

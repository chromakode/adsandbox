# Simple sandboxed multiple-frame ads

This code demonstrates a method of populating an arbitrary number of sandboxed ads from a single iframe.

Tested to work on IE6+, Firefox 3+, Chrome, Opera 11+.

An initial iframe "ad_main" is loaded, which contains information about all ads to be displayed on the page. The "ad_main" frame signals the parent page that "child" ad frames must be created via `postMessage` or a cross-domain iframe as a fallback. Child ad frames load a document containing a script that fetches their contents from the JavaScript scope of "ad_main".

To run this demo, you should create localhost aliases for "home.local" and "ads.local" in your `/etc/hosts` file (or similar):

    127.0.0.1	home.local ads.local
